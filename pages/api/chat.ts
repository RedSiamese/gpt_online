import { NextApiRequest, NextApiResponse } from 'next';
import fetch from 'node-fetch';
import { isServiceOpen } from '../../utils/serviceStatus';

export default async function handler(req: NextApiRequest, res: NextApiResponse) {
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  const { messages } = req.body;

  // 检查服务状态
  if (!isServiceOpen()) {
    return res.status(503).json({ error: '服务已关闭' });
  }

  try {
    const controller = new AbortController();
    const timeoutId = setTimeout(() => controller.abort(), 8000); // 设置超时时间为8秒

    const response = await fetch('https://api.openai.com/v1/chat/completions', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${process.env.NEXT_PUBLIC_OPENAI_API_KEY}`, // 读取环境变量中的API密钥
      },
      body: JSON.stringify({
        model: 'gpt-4o-mini',
        messages,
      }),
      signal: controller.signal,
    });

    clearTimeout(timeoutId);

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    const data = await response.json();
    res.status(200).json(data);
  } catch (error) {
    if (error instanceof Error) {
      if (error.name === 'AbortError') {
        console.error('Request aborted due to service closure or timeout');
        res.status(503).json({ error: '服务已关闭或请求超时' });
      } else if ('code' in error && error.code === 'ETIMEDOUT') {
        console.error('Request timed out');
        res.status(504).json({ error: 'AI请求超时，请稍后再试' });
      } else {
        console.error('Error calling OpenAI API:', error);
        res.status(500).json({ error: 'Error calling OpenAI API' });
      }
    } else {
      console.error('Unexpected error:', error);
      res.status(500).json({ error: 'Unexpected error' });
    }
  }
}
