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

// 添加 GitLab 文件获取函数
async function fetchGitLabContent(url: string): Promise<string | null> {
  try {
    // 转换 GitLab URL 为原始内容 URL
    const rawUrl = url
      .replace('/-/blob/', '/-/raw/')
      .replace(/\/-\/tree\/[^\/]+\//, '/-/raw/');
    
    const response = await axios.get(rawUrl);
    return `GitLab文件内容 (${url}):\n\n${response.data}`;
  } catch (error) {
    console.error('Error fetching GitLab content:', error);
    return null;
  }
}

// 添加 GitLab Wiki 文件获取函数
async function fetchGitLabWikiContent(url: string): Promise<string | null> {
  try {
    // 转换 GitLab Wiki URL 为原始内容 URL
    const wikiUrl = url.replace('/-/wikis/', '/-/raw/master/');
    const response = await axios.get(wikiUrl);
    return `GitLab Wiki文件内容 (${url}):\n\n${response.data}`;
  } catch (error) {
    console.error('Error fetching GitLab Wiki content:', error);
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
          // 更新正则表达式，添加 Wiki 支持
          const githubRegex = /https:\/\/github\.com\/[^\/]+\/[^\/]+\/blob\/[^\/]+\/[^\s]+/;
          const gitlabRegex = /https:\/\/(?:gitlab\.com|[^\/]+\/gitlab)[^\/]*\/[^\/]+\/[^\/]+\/-\/(?:blob|tree)\/[^\/]+\/[^\s]+/;
          const gitlabWikiRegex = /https:\/\/(?:gitlab\.com|[^\/]+\/gitlab)[^\/]*\/[^\/]+\/[^\/]+\/-\/wikis\/[^\s]+/;
          
          if (githubRegex.test(identifier)) {
            content = await fetchGitHubContent(identifier);
          } else if (gitlabWikiRegex.test(identifier)) {
            content = await fetchGitLabWikiContent(identifier);
          } else if (gitlabRegex.test(identifier)) {
            content = await fetchGitLabContent(identifier);
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
      model: 'gpt-4o-mini',
      messages: fullMessages,
      stream: true,
    });

    for await (const chunk of stream) {
      const choice = chunk.choices[0];
      const content = choice?.delta?.content || "";
      const finishReason = choice?.finish_reason || "unknown";
  
      // 发送内容片段（如果有）
      if (content) {
        res.write(`data: ${JSON.stringify({ content })}\n\n`);
      }
  
      // 检测结束标记
      if (finishReason === "stop") {
        // 发送 OpenAI 官方约定的结束标记 [DONE]
        res.write(`data: ${JSON.stringify({ content:"[DONE]" })}\n\n`);
        break; // 主动跳出循环
      }
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
