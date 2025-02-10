import { NextApiRequest, NextApiResponse } from 'next';
import fs from 'fs';
import path from 'path';

export default function handler(req: NextApiRequest, res: NextApiResponse) {
  const { dir } = req.query;
  if (!dir || typeof dir !== 'string') {
    return res.status(400).json({ error: 'Invalid directory name' });
  }

  const dirPath = path.join(process.cwd(), 'docs', dir);
  if (!fs.existsSync(dirPath) || !fs.statSync(dirPath).isDirectory()) {
    return res.status(404).json({ error: 'Directory not found' });
  }

  const files = fs.readdirSync(dirPath);
  let content = '';
  files.forEach((file) => {
    const filePath = path.join(dirPath, file);
    const fileContent = fs.readFileSync(filePath, 'utf-8');
    content += `文件名: ${file}\n\`\`\`${fileContent}\n\n\`\`\``;
  });

  res.status(200).json({ content });
}
