import React from "react";

const ChatMessage = ({ sender, text }) => {
  return (
    <div className={`message ${sender}`}>
      <strong>{sender === "user" ? "You" : "AI"}:</strong> {text}
    </div>
  );
};

export default ChatMessage;