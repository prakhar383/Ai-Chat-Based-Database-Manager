import React from "react";
import InteractionForm from "./components/InteractionForm";
import ChatInterface from "./components/ChatInterface";
import "./App.css";

function App() {
  return (
    <div className="app-container">
      <div className="left-panel">
        <h2>Live Database Preview</h2>
        <InteractionForm />
      </div>

      <div className="right-panel">
        <h2>Ai Data Assistant</h2>
        <ChatInterface />
      </div>
    </div>
  );
}

export default App;