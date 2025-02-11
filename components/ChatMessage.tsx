import React, { useEffect, useState } from 'react';
import ReactMarkdown from 'react-markdown';
import styles from '../styles/Chat.module.css';

interface Message {
  text: string;
  sender: 'user' | 'ai' | 'system';
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
    </div>
  );
};

export default ChatMessage;
