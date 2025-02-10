import { NextApiRequest, NextApiResponse } from 'next';
import { setServiceOpen } from '../../utils/serviceStatus';

export default function handler(req: NextApiRequest, res: NextApiResponse) {
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  const { command } = req.body;

  if (command === '!close') {
    setServiceOpen(false);
    return res.status(200).json({ message: '服务已关闭' });
  }

  if (command === '!open') {
    setServiceOpen(true);
    return res.status(200).json({ message: '服务已开启' });
  }

  return res.status(400).json({ error: 'Invalid command' });
}
