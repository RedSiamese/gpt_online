"use client";

import React, { useState } from 'react';
import ChatInput from '../../components/ChatInput';
import ChatMessage from '../../components/ChatMessage';
import styles from '../../styles/Chat.module.css';

interface Message {
  text: string;
  sender: 'user' | 'ai' | 'system';
  requestTokens?: number;
  responseTokens?: number;
}

const Chat = () => {
  const [messages, setMessages] = useState<Message[]>([]);
  const [docsContent, setDocsContent] = useState<{ [key: string]: string }>({});

  const fetchDocsContent = async (dirName: string) => {
    try {
      const response = await fetch(`/api/readDocs?dir=${dirName}`);
      const data = await response.json();
      setDocsContent((prev) => ({ ...prev, [dirName]: data.content }));
      return data.content;
    } catch (error) {
      console.error('Error fetching docs content:', error);
      return '';
    }
  };

  const handleSendMessage = async (message: string) => {
    const userMessage: Message = { text: message, sender: 'user', requestTokens: 0 };
    const newMessages = [...messages, userMessage];
    setMessages(newMessages);

    // 处理!close和!open命令
    if (message === '!close' || message === '!open') {
      try {
        const response = await fetch('/api/control', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ command: message }),
        });

        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();
        setMessages([...newMessages, { text: data.message, sender: 'system' }]);
        return;
      } catch (error) {
        console.error('Error calling control API:', error);
        setMessages([...newMessages, { text: '控制命令执行失败，请稍后再试。', sender: 'system' }]);
        return;
      }
    }

    // 只保留最近20次的历史对话
    const recentMessages = newMessages.slice(-20);

    // 构建上下文
    let context = recentMessages.map((msg) => ({
      role: msg.sender === 'user' ? 'user' : 'assistant',
      content: msg.text,
    }));

    // 如果用户输入包含 "@xxx "，则解析出xxx，并在docs目录中搜索该名字的目录
    const match = message.match(/@(\S+)\s/);
    if (match) {
      const dirName = match[1];
      let dirContent = docsContent[dirName];
      if (!dirContent) {
        dirContent = await fetchDocsContent(dirName);
      }
      if (dirContent) {
        context = [
          { role: 'system', content: dirContent },
          ...context,
        ];
      }
    }

    // 调用新的API路由
    try {
      const response = await fetch('/api/chat', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ messages: context }),
      });

      if (!response.ok) {
        if (response.status === 503) {
          setMessages([...newMessages, { text: '服务已关闭', sender: 'system' }]);
        } else if (response.status === 504) {
          setMessages([...newMessages, { text: 'AI请求超时，请稍后再试', sender: 'system' }]);
        } else {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return;
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
      setMessages([...newMessages, { text: 'AI回复失败，请稍后再试。', sender: 'system' }]);
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
