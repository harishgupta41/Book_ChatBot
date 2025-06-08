from faker import Faker
from random import randint, uniform, choice
from dbConfig import create_app, db
from models import Book

fake = Faker()
app = create_app()

GENRES = ['Fiction', 'Sci-Fi', 'Fantasy', 'Mystery', 'Romance', 'Thriller', 'Non-fiction', 'Biography']

def generate_books(n=100):
    books = []
    for _ in range(n):
        book = Book(
            title=fake.sentence(nb_words=4).replace('.', ''),
            author=fake.name(),
            genre=choice(GENRES),
            price=round(uniform(100, 1000), 2),
            rating=round(uniform(1.0, 5.0), 1),
            description=fake.text(max_nb_chars=200)
        )
        books.append(book)
    return books

with app.app_context():
    db.create_all()
    db.session.add_all(generate_books())
    db.session.commit()
    print("✅ Inserted 100 mock books into the database.")
