import React from 'react';
import ReactMarkdown from 'react-markdown';
import styles from '../styles/Chat.module.css';

const ChatMessage = ({ message }) => {
  return (
    <div className={`${styles.message} ${message.sender === 'ai' ? styles.aiMessage : styles.userMessage}`}>
      <ReactMarkdown>{message.text}</ReactMarkdown>
      {message.sender === 'user' && message.requestTokens > 0 && (
        <div className={styles.tokenCount}>请求Tokens: {message.requestTokens}</div>
      )}
      {message.sender === 'ai' && (
        <div className={styles.tokenCount}>回复Tokens: {message.responseTokens}</div>
      )}
    </div>
  );
};

export default ChatMessage;
