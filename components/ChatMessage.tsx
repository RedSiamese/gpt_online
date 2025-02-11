import React from 'react';
import ReactMarkdown from 'react-markdown';
import styles from '../styles/Chat.module.css';

interface Message {
  text: string;
  sender: 'user' | 'ai' | 'system';
  timestamp?: string;
}

const ChatMessage: React.FC<{ message: Message }> = ({ message }) => {
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
      <ReactMarkdown>{message.text}</ReactMarkdown>
      {message.timestamp && (
        <div className={styles.timestamp}>{message.timestamp}</div>
      )}
    </div>
  );
};

export default ChatMessage;
