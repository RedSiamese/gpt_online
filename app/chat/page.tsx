"use client";
import React, { useState } from 'react';
import ChatInput from '../../components/ChatInput';
import ChatMessage from '../../components/ChatMessage';
import styles from '../../styles/Chat.module.css';

interface Message {
  text: string;
  sender: 'user' | 'ai' | 'system';
  timestamp?: string;
}

const Chat = () => {
  const [messages, setMessages] = useState<Message[]>([]);

  const formatTime = () => {
    const now = new Date();
    return now.toLocaleTimeString('zh-CN', { 
      hour: '2-digit', 
      minute: '2-digit',
      hour12: false 
    });
  };

  const handleSendMessage = async (message: string) => {
    const userMessage: Message = { 
      text: message, 
      sender: 'user',
      timestamp: formatTime()  // 为用户消息添加时间戳
    };
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
        setMessages([...newMessages, { 
          text: data.message, 
          sender: 'system',
          timestamp: formatTime()
        }]);
        return;
      } catch (error) {
        console.error('Error calling control API:', error);
        setMessages([...newMessages, { 
          text: '控制命令执行失败，请稍后再试。', 
          sender: 'system',
          timestamp: formatTime()
        }]);
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
          setMessages([...newMessages, { 
            text: '服务已关闭', 
            sender: 'system',
            timestamp: formatTime()
          }]);
        } else if (response.status === 504) {
          setMessages([...newMessages, { 
            text: 'AI请求超时，请稍后再试', 
            sender: 'system',
            timestamp: formatTime()
          }]);
        } else {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return;
      }

      // 创建一个空的 AI 响应消息
      const aiMessage: Message = { text: '', sender: 'ai' };
      setMessages([...newMessages, aiMessage]);

      const reader = response.body?.getReader();
      const decoder = new TextDecoder();
      if (!reader) throw new Error('No reader available');

      while (true) {
        const { done, value } = await reader.read();
        if (done) { console.log('end: done'); break; }

        const chunk = decoder.decode(value);
        const lines = chunk.split('\n');
        
        for (const line of lines) {
          if (line.startsWith('data: ')) {
            const data = line.slice(5);
            if (data === ' [DONE]') { break; }

            try {
              const { content } = JSON.parse(data);
              setMessages(prev => {
                const updated = [...prev];
                const lastMessage = updated[updated.length - 1];
                if (lastMessage.sender === 'ai') {
                  lastMessage.text += content;
                }
                return updated;
              });
            } catch (e) {
              console.error('Error parsing chunk:', e);
            }
          } else {
          console.log('Error line:', line);
        }
        }
      }

      // 在流式输出完成后添加时间戳
      setMessages(prev => {
        const updated = [...prev];
        const lastMessage = updated[updated.length - 1];
        if (lastMessage.sender === 'ai') {
          lastMessage.timestamp = formatTime();
        }
        return updated;
      });

    } catch (error) {
      console.error('Error calling OpenAI API:', error);
      setMessages([...newMessages, { 
        text: 'AI回复失败，请稍后再试。', 
        sender: 'system',
        timestamp: formatTime()
      }]);
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
