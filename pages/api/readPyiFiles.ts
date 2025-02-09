import { NextApiRequest, NextApiResponse } from 'next';
import fs from 'fs';
import path from 'path';

export default function handler(req: NextApiRequest, res: NextApiResponse) {
  const pyiDir = path.join(process.cwd(), 'docs/pyi');
  const files = fs.readdirSync(pyiDir);
  let content = '这些pyi文件是python扩展包pycluster2x的注解文件，描述了其中定义的各种类和类方法的定义。\n\n';
  files.forEach((file) => {
    const filePath = path.join(pyiDir, file);
    const fileContent = fs.readFileSync(filePath, 'utf-8');
    content += `文件名: ${file}\n${fileContent}\n\n`;
  });
  res.status(200).json({ content });
}
