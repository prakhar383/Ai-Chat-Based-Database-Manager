import React from "react";
import InteractionForm from "./components/InteractionForm";
import ChatInterface from "./components/ChatInterface";
import "./App.css";

function App() {
  return (
    <div className="app-container">
      <div className="left-panel">
        <h2>Interaction Details</h2>
        <InteractionForm />
      </div>

      <div className="right-panel">
        <h2>AI Assistant</h2>
        <ChatInterface />
      </div>
    </div>
  );
}

export default App;