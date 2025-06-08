from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user
from models import User,Book, ChatLog
from dbConfig import db
from flask import Blueprint, request, jsonify
from chatbot import parse_message,search_books

auth_bp = Blueprint('auth', __name__)
book_bp = Blueprint('book', __name__)

# Signup API
@auth_bp.route('/signup', methods=['POST'])
def signup():
    data = request.json
    username = data['username']
    password = data['password']

    if User.query.filter_by(username=username).first():
        return jsonify({'message': 'User already exists'}), 409

    hashed_password = generate_password_hash(password)
    new_user = User(username=username, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'Signup successful'}), 201

# Login API
@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data['username']
    password = data['password']

    user = User.query.filter_by(username=username).first()
    if not user or not check_password_hash(user.password, password):
        return jsonify({'message': 'Invalid credentials'}), 401

    login_user(user)
    return jsonify({'message': 'Login successful'}), 200

# Logout API
@auth_bp.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return jsonify({'message': 'Logged out'}), 200

# Chatting API
@book_bp.route('/chat', methods=['POST'])
@login_required
def chat():
    data = request.json
    message = data['message']

    filters = parse_message(message)
    books = search_books(filters)

    if books:
        response = f"📚 Found {len(books)} book(s):\n"
        for book in books:
            response += f"\n• \"{book.title}\" by {book.author} — ₹{book.price}, ⭐{book.rating}"
    else:
        response = "Sorry, I couldn't find any books matching your query."

    # Save to chat log
    log = ChatLog(user_id=current_user.id, message=message, response=response)
    db.session.add(log)
    db.session.commit()

    return jsonify({'response': response})