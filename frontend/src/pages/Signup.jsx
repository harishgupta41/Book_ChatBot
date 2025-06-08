import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import api from "../api";
import './Signup.css';

export default function Signup() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const navigate = useNavigate();

  const handleSignup = async (e) => {
    e.preventDefault();
    try {
      await api.post("/signup", { username, password });
      alert("Signup successful!");
      navigate("/login");
    } catch (err) {
      const msg = err.response?.data?.message || "Signup failed";
      alert(msg);
    }
  };

  return (
    <div className="signup-container">
      <h2>Register</h2>
      <form onSubmit={handleSignup}>
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
        <button type="submit">Signup</button>
      </form>
      <div className="redirect">
        Already have an account?
        <button onClick={() => navigate("/login")}>Login</button>
      </div>
    </div>
  );
}
