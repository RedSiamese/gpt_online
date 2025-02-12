import { NextApiRequest, NextApiResponse } from 'next';
import fs from 'fs/promises';
import path from 'path';
import OpenAI, { APIError } from 'openai';
import { isServiceOpen } from '../../utils/serviceStatus';
import axios from 'axios';

const openai = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY,
});

async function readDocsContent(dirName: string): Promise<string | null> {
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
    return null;
  }
}

async function fetchGitHubContent(url: string): Promise<string | null> {
  try {
    const rawUrl = url
      .replace('github.com', 'raw.githubusercontent.com')
      .replace('/blob/', '/');
    const response = await axios.get(rawUrl);
    return `GitHub文件内容 (${url}):\n\n${response.data}`;
  } catch (error) {
    console.error('Error fetching GitHub content:', error);
    return null;
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

    const lastUserMessage = messages[messages.length - 1];
    if (lastUserMessage.role === 'user') {
      const match = lastUserMessage.content.match(/@(\S+)/);
      if (match) {
        const identifier = match[1];
        let content = await readDocsContent(identifier);
        
        if (!content) {
          // 检查是否为GitHub链接
          const githubRegex = /https:\/\/github\.com\/[^\/]+\/[^\/]+\/blob\/[^\/]+\/[^\s]+/;
          if (githubRegex.test(identifier)) {
            content = await fetchGitHubContent(identifier);
          }
        }

        if (content) {
          systemContext = content;
        }
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
      model: 'o3-mini',
      messages: fullMessages,
      stream: true,
    });

    for await (const chunk of stream) {
      const content = chunk.choices[0]?.delta?.content || '';
      res.write(`data: ${JSON.stringify({ content })}\n\n`);
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
