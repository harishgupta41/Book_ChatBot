import re
from models import Book
# Extract intent and filters from message
def parse_message(message):
    # print("this is message parsing\n\n\n\n")
    filters = {}

    # Genre detection
    genres = ['fiction', 'sci-fi', 'fantasy', 'mystery', 'romance', 'thriller', 'non-fiction', 'biography']
    for genre in genres:
        if genre in message.lower():
            filters['genre'] = genre.title()
            break

    # Price detection (e.g., "under 500", "below 700")
    price_match = re.search(r'(under|below)\s*₹?(\d+)', message.lower())
    if price_match:
        filters['price'] = float(price_match.group(2))

    # Rating detection
    rating_match = re.search(r'rating\s*(above|over|greater than)\s*(\d(\.\d)?)', message.lower())
    if rating_match:
        filters['rating'] = float(rating_match.group(2))

    # Author name (e.g., "by Rowling")
    author_match = re.search(r'by\s+([a-zA-Z\s]+)', message)
    if author_match:
        filters['author'] = author_match.group(1).strip()

    # print(filters)
    return filters

def search_books(filters):
    query = Book.query

    if 'genre' in filters:
        query = query.filter(Book.genre.ilike(f"%{filters['genre']}%"))
    if 'price' in filters:
        query = query.filter(Book.price <= filters['price'])
    if 'rating' in filters:
        query = query.filter(Book.rating >= filters['rating'])
    if 'author' in filters:
        query = query.filter(Book.author.ilike(f"%{filters['author']}%"))
     
    books = query.all()
    return books