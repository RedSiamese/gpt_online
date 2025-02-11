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

  const handleSendMessage = async (message: string) => {
    const userMessage: Message = { text: message, sender: 'user', requestTokens: 0 };
    const newMessages = [...messages, userMessage];
    setMessages(newMessages);

    // 处理!close和!open命令
    if (message === '!close' || message === '!open') {
      try {
        const response = await fetch('/api/control', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
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

    try {
      const response = await fetch('/api/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ 
          messages: newMessages.slice(-20).map(msg => ({
            role: msg.sender === 'user' ? 'user' : 'assistant',
            content: msg.text
          }))
        }),
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
