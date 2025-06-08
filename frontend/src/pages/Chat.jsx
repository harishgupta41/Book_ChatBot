import React, { useState, useEffect, useRef } from "react";
import { useNavigate } from "react-router-dom";
import api from "../api";
import "./Chat.css";

export default function Chat() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const chatEndRef = useRef(null);
  const navigate = useNavigate();

  useEffect(() => {
    chatEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  const sendMessage = async () => {
    if (!input.trim()) return;
    const time = new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
    const userMessage = { sender: "user", text: input, time };
    setMessages(prev => [...prev, userMessage]);

    try {
      const res = await api.post("/chat", { message: input });
      const botMessage = {
        sender: "bot",
        text: res.data.response,
        time: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
      };
      setMessages(prev => [...prev, botMessage]);
    } catch {
      setMessages(prev => [...prev, {
        sender: "bot",
        text: "❌ Server error",
        time
      }]);
    }

    setInput("");
  };

  const resetChat = () => {
    setMessages([]);
  };

  const logout = async () => {
    try {
      await api.post("/logout");
      alert('Logout Success');
      navigate("/login");
    } catch (err) {
      alert("Logout failed");
    }
  };

  return (
    <div className="chat-container">
      <div className="chat-header">
        <h2>📚 Book Chatbot</h2>
        <div>
          <button onClick={resetChat} className="reset-button">Reset Chat</button>
          <button onClick={logout} className="logout-button">Logout</button>
        </div>
      </div>

      <div className="chat-box">
        {messages.map((msg, i) => (
          <div key={i} className="chat-message" style={{ justifyContent: msg.sender === "user" ? "flex-end" : "flex-start" }}>
            {msg.sender === "bot" && (
              <img src="https://cdn-icons-png.flaticon.com/512/4712/4712027.png" alt="Bot" className="chat-avatar" />
            )}
            <div className={`chat-bubble ${msg.sender === "bot" ? "bot" : ""}`}>
              <strong>{msg.sender === "user" ? "You" : "Bot"}</strong>
              <small>{msg.time}</small>
              <div style={{ whiteSpace: "pre-wrap", marginTop: 4 }}>{msg.text}</div>
            </div>
            {msg.sender === "user" && (
              <img src="https://cdn-icons-png.flaticon.com/512/1144/1144760.png" alt="You" className="chat-avatar" />
            )}
          </div>
        ))}
        <div ref={chatEndRef} />
      </div>

      <div className="chat-input">
        <input
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={(e) => e.key === "Enter" && sendMessage()}
          placeholder="Type a message..."
        />
        <button onClick={sendMessage}>Send</button>
      </div>
    </div>
  );
}
