from dbConfig import create_app
from routes import auth_bp, book_bp

# Creating flask app
app = create_app()

# Creating tables in database if not exist
with app.app_context():
    from models import db
    db.create_all()

# Creating blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(book_bp)

if __name__ == '__main__':
    app.run(debug=True)
