import { NextApiRequest, NextApiResponse } from 'next';
import fs from 'fs/promises';
import path from 'path';
import OpenAI, { APIError } from 'openai';
import { isServiceOpen } from '../../utils/serviceStatus';

const openai = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY,
});

async function readDocsContent(dirName: string): Promise<string> {
  try {
    const docsDir = path.join(process.cwd(), 'docs', dirName);
    const files = await fs.readdir(docsDir);
    const contents = await Promise.all(
      files.map(async (file) => {
        const content = await fs.readFile(path.join(docsDir, file), 'utf-8');
        return content;
      })
    );
    return contents.join('\n\n');
  } catch (error) {
    console.error('Error reading docs:', error);
    return '';
  }
}

export default async function handler(req: NextApiRequest, res: NextApiResponse) {
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  // 检查服务状态
  if (!isServiceOpen()) {
    return res.status(503).json({ error: '服务已关闭' });
  }

  try {
    const { messages } = req.body;
    let systemContext = '';

    // 检查最后一条用户消息是否包含 @指令
    const lastUserMessage = messages[messages.length - 1];
    if (lastUserMessage.role === 'user') {
      const match = lastUserMessage.content.match(/@(\S+)\s/);
      if (match) {
        const dirName = match[1];
        systemContext = await readDocsContent(dirName);
      }
    }

    // 构建完整的消息数组
    const fullMessages = systemContext
      ? [{ role: 'system', content: systemContext }, ...messages]
      : messages;

    // 设置流式响应头
    res.writeHead(200, {
      'Content-Type': 'text/event-stream',
      'Cache-Control': 'no-cache, no-transform',
      'Connection': 'keep-alive',
    });

    const stream = await openai.chat.completions.create({
      model: 'gpt-4o-mini',
      messages: fullMessages,
      stream: true,
    });

    for await (const chunk of stream) {
      const content = chunk.choices[0]?.delta?.content || '';
      const usage = chunk.usage; // 从每个chunk中获取usage信息
      
      res.write(`data: ${JSON.stringify({ 
        content,
        usage,
        final: !content && usage // 当content为空且有usage时，说明是最后一个chunk
      })}\n\n`);
    }

    res.end('data: [DONE]\n\n');

  } catch (error: unknown) {
    console.error('Error:', error);
    
    if (error instanceof APIError) {
      res.status(error.status || 500).json({ 
        error: error.message || 'OpenAI API error occurred'
      });
    } else if (error instanceof Error) {
      res.status(500).json({ 
        error: error.message || 'An unexpected error occurred' 
      });
    } else {
      res.status(500).json({ 
        error: 'An unknown error occurred' 
      });
    }
  }
}
