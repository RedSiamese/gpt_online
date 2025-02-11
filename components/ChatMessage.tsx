import React, { useEffect, useState } from 'react';
import ReactMarkdown from 'react-markdown';
import styles from '../styles/Chat.module.css';

interface Message {
  text: string;
  sender: 'user' | 'ai' | 'system';
  requestTokens?: number;
  responseTokens?: number;
}

const ChatMessage: React.FC<{ message: Message }> = ({ message }) => {
  const [displayedText, setDisplayedText] = useState(message.text);

  useEffect(() => {
    if (message.sender === 'ai') {
      setDisplayedText(message.text);
    }
  }, [message.text, message.sender]);

  const renderText = (text: string) => {
    const parts = text.split(/(@\S+)/g);
    return parts.map((part, index) =>
      part.startsWith('@') ? (
        <span key={index} className={styles.highlight}>
          {part}
        </span>
      ) : (
        <ReactMarkdown key={index}>{part}</ReactMarkdown>
      )
    );
  };

  return (
    <div
      className={`${styles.message} ${
        message.sender === 'ai'
          ? styles.aiMessage
          : message.sender === 'system'
          ? styles.systemMessage
          : styles.userMessage
      }`}
    >
      <div>{renderText(displayedText)}</div>
      {message.sender === 'user' && message.requestTokens !== undefined && message.requestTokens > 0 && (
        <div className={styles.tokenCount}>请求Tokens: {message.requestTokens}</div>
      )}
      {message.sender === 'ai' && message.responseTokens !== undefined && (
        <div className={styles.tokenCount}>回复Tokens: {message.responseTokens}</div>
      )}
    </div>
  );
};

export default ChatMessage;
