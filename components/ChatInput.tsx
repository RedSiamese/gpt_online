import React, { useState } from 'react';
import styles from '../styles/Chat.module.css';

const ChatInput = ({ onSendMessage }) => {
  const [input, setInput] = useState('');

  const handleSend = () => {
    if (input.trim()) {
      onSendMessage(input);
      setInput('');
    }
  };

  const handleKeyDown = (e) => {
    if (e.key === 'Enter') {
      if (e.ctrlKey) {
        // Ctrl+Enter 换行
        setInput(input + '\n');
      } else {
        // Enter 发送消息
        e.preventDefault();
        handleSend();
      }
    }
  };

  return (
    <div className={styles.inputContainer}>
      <textarea
        value={input}
        onChange={(e) => setInput(e.target.value)}
        onKeyDown={handleKeyDown}
        className={styles.input}
        placeholder="输入消息..."
      />
      <button onClick={handleSend} className={styles.sendButton}>
        发送
      </button>
    </div>
  );
};

export default ChatInput;
