from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash,generate_password_hash
from flask_login import LoginManager
from flask import Flask
from flask_cors import CORS

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.secret_key = 'uplyftsecretkey'

    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:harish9650@localhost/chatbot'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    login_manager.init_app(app)

    CORS(app,supports_credentials=True)

    from models import User
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    return app
