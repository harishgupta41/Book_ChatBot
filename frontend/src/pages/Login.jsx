import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import api from "../api";
import './Login.css';

export default function Login() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const navigate = useNavigate();

  const handleLogin = async (e) => {
    e.preventDefault();
    try {
      await api.post("/login", { username, password });
      navigate("/chat");
    } catch (err) {
      const msg = err.response?.data?.message || "Login failed";
      alert(msg);
    }
  };

  return (
    <div className="login-container">
      <h2>Login</h2>
      <form onSubmit={handleLogin}>
        <input
          placeholder="Username"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          required
        />
        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
        />
        <button type="submit">Login</button>
      </form>
      <div className="redirect">
        New user?
        <button onClick={() => navigate("/")}>Signup</button>
      </div>
    </div>
  );
}
