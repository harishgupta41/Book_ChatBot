# Book_ChatBot

This is a full-stack web application that simulates an e-commerce **sales chatbot** for a **bookstore**. It allows users to sign up, log in, and chat with a rule-based bot to search and explore books from a mock inventory. Built using **React (frontend)** and **Flask (backend)** with **MySQL**.

---

## 🚀 Features

- 🔐 **User Authentication**: Signup, login, logout with secure session handling.
- 🤖 **Rule-Based Chatbot**: Understands search queries by genre, price, rating, and author.
- 📚 **Book Search API**: Filters books using REST API backed by a 100+ item mock inventory.
- 🗃️ **Chat History**: Stores user-bot conversations in the database.
- 💬 **Chat UI**: Custom-styled React chatbot with avatars, timestamps, reset, and scroll.
- 🖼️ **Responsive Design**: Clean interface compatible with desktops and laptops.
- ⚙️ **Modular Code**: Separated components for scalability and readability.

---

## 🛠️ Tech Stack

| Layer        | Tech Used                   |
|--------------|-----------------------------|
| Frontend     | React, Axios, Custom CSS    |
| Backend      | Flask, Flask-Login, Flask-CORS |
| Database     | MySQL                       |
| ORM          | SQLAlchemy                  |
| Auth Security| Werkzeug (password hashing) |

---


---

## 🔄 Setup Instructions

### 🧱 Backend (Flask + MySQL)
1. Run the following script
```
cd backend
python -m venv venv
venv\Scripts\activate   # or source venv/bin/activate on Linux/mac
pip install -r requirements.txt
```

2. Create MySQL Database
```
create database chatbot;
```
3. Update your **dbConfig.py** file

4. Seed fake entries in database
```
python seedData.py 
```

5. Start Server

```
python app.py
```
### 🎨 Frontend (React)
```
cd frontend
npm install
npm start
```
---
##### The app runs at:
<small>
🔗 http://localhost:3000 (frontend)<br>
🔗 http://localhost:5000 (backend)
</small>

---
## 🧠 Sample Chatbot Queries
- Show me thriller books under 500

- Find books by J.K. Rowling

- Books with rating above 4.2

- I want romance books below ₹300
---
## 📄 Learnings
- Built a complete full-stack app with auth, DB, APIs, and UI integration.

- Understood CORS, session handling, and cross-origin frontend-backend communication.

- Practiced modular code structure and reusable components.