import React, { useState, useRef, useEffect } from "react";
import axios from "axios";
import { useDispatch, useSelector } from "react-redux";
import { addMessage } from "../redux/interactionSlice";
import ChatMessage from "./ChatMessage";

const ChatInterface = () => {
  const [input, setInput] = useState("");
  const dispatch = useDispatch();
  const messages = useSelector((state) => state.interaction.chatMessages);
  const messagesEndRef = useRef(null);

  const sendMessage = async () => {
    if (!input.trim()) return;

    // Save user message to Redux and clear input
    dispatch(addMessage({ sender: "user", text: input }));
    const messageToSend = input;
    setInput("");

    try {
      const response = await axios.post("http://127.0.0.1:8000/chat/", {
        message: messageToSend
      });

      // Update Redux with the AI's reply
      dispatch(addMessage({ sender: "ai", text: response.data.reply }));
    } catch (error) {
      dispatch(addMessage({ sender: "ai", text: "Error contacting AI Agent." }));
    }
  };

  // Auto-scroll to bottom of chat
  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  return (
    <div className="chat-container">
      <div className="chat-header">
        <h3>🤖 AI Assistant</h3>
        <p>Log interaction via chat</p>
      </div>
      <div className="chat-messages">
        {messages.map((msg, index) => (
          <ChatMessage key={index} sender={msg.sender} text={msg.text} />
        ))}
        <div ref={messagesEndRef} />
      </div>

      <div className="chat-input-area">
        <input
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyPress={(e) => e.key === 'Enter' && sendMessage()}
          placeholder="Describe interaction..."
        />
        <button onClick={sendMessage}>Send</button>
      </div>
    </div>
  );
};

export default ChatInterface;