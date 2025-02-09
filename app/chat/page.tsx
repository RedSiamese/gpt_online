"use client";

import React, { useState, useEffect } from 'react';
import ChatInput from '../../components/ChatInput';
import ChatMessage from '../../components/ChatMessage';
import styles from '../../styles/Chat.module.css';

interface Message {
  text: string;
  sender: 'user' | 'ai';
  requestTokens?: number;
  responseTokens?: number;
}

const Chat = () => {
  const [messages, setMessages] = useState<Message[]>([]);
  const [pyiFilesContent, setPyiFilesContent] = useState('');

  useEffect(() => {
    // 调用API获取docs/pyi/目录中的所有文件内容
    const fetchPyiFilesContent = async () => {
      try {
        const response = await fetch('/api/readPyiFiles');
        const data = await response.json();
        setPyiFilesContent(data.content);
      } catch (error) {
        console.error('Error fetching pyi files content:', error);
      }
    };

    fetchPyiFilesContent();
  }, []);

  const handleSendMessage = async (message: string) => {
    const userMessage: Message = { text: message, sender: 'user', requestTokens: 0 };
    const newMessages = [...messages, userMessage];
    setMessages(newMessages);

    // 只保留最近20次的历史对话
    const recentMessages = newMessages.slice(-20);

    // 构建上下文
    let context = recentMessages.map((msg) => ({
      role: msg.sender === 'user' ? 'user' : 'assistant',
      content: msg.text,
    }));

    // 如果用户输入包含 "@pycluster2x"，则添加pycluster2x上下文
    if (message.includes('@pycluster2x ')) {
      context = [
        { role: 'system', content: '这些pyi文件是python扩展包pycluster2x的注解文件，描述了其中定义的各种类和类方法的定义。\n\n' + pyiFilesContent },
        ...context,
      ];
    }

    // 调用OpenAI ChatGPT API
    try {
      const response = await fetch('https://api.openai.com/v1/chat/completions', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${process.env.NEXT_PUBLIC_OPENAI_API_KEY}`, // 读取环境变量中的API密钥
        },
        body: JSON.stringify({
          model: 'gpt-4o-mini',
          messages: context,
        }),
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const data = await response.json();
      const aiMessage = data.choices[0].message.content;
      const requestTokens = data.usage.prompt_tokens;
      const responseTokens = data.usage.completion_tokens;

      // 更新用户消息的请求token数
      newMessages[newMessages.length - 1].requestTokens = requestTokens;

      setMessages([...newMessages, { text: aiMessage, sender: 'ai', responseTokens }]);
    } catch (error) {
      console.error('Error calling OpenAI API:', error);
      setMessages((prevMessages) => [
        ...prevMessages,
        { text: 'AI回复失败，请稍后再试。', sender: 'ai', responseTokens: 0 },
      ]);
    }
  };

  return (
    <div className={styles.chatContainer}>
      <div className={styles.messagesContainer}>
        {messages.map((msg, index) => (
          <ChatMessage key={index} message={msg} />
        ))}
      </div>
      <ChatInput onSendMessage={handleSendMessage} />
    </div>
  );
};

export default Chat;
