from dbConfig import db
from flask_login import UserMixin

# User class for creating users
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

# Book class for creating books
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    author = db.Column(db.String(255))
    genre = db.Column(db.String(100))
    price = db.Column(db.Numeric(10, 2))
    rating = db.Column(db.Float)
    description = db.Column(db.Text)

# Chatlog class for logging individual chat messages and responses
class ChatLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    message = db.Column(db.Text)
    response = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, server_default=db.func.now())
