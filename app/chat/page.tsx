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

      // 创建一个空的 AI 响应消息
      const aiMessage: Message = { text: '', sender: 'ai', responseTokens: 0 };
      setMessages([...newMessages, aiMessage]);

      const reader = response.body?.getReader();
      const decoder = new TextDecoder();

      if (!reader) throw new Error('No reader available');

      while (true) {
        const { done, value } = await reader.read();
        if (done) break;

        const chunk = decoder.decode(value);
        const lines = chunk.split('\n');
        
        for (const line of lines) {
          if (line.startsWith('data: ')) {
            const data = line.slice(5);
            if (data === '[DONE]') break;

            try {
              const { 
                content, 
                usage
              } = JSON.parse(data);

              setMessages(prev => {
                const updated = [...prev];
                const lastMessage = updated[updated.length - 1];
                if (lastMessage.sender === 'ai') {
                  if (content) {
                    lastMessage.text += content;
                  }
                  if (usage) {
                    lastMessage.responseTokens = usage.completion_tokens;
                    // 更新上一条用户消息的请求tokens
                    if (updated.length > 1) {
                      const userMessage = updated[updated.length - 2];
                      if (userMessage.sender === 'user') {
                        userMessage.requestTokens = usage.prompt_tokens;
                      }
                    }
                  }
                }
                return updated;
              });
            } catch (e) {
              console.error('Error parsing chunk:', e);
            }
          }
        }
      }

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
