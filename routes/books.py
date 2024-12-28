from flask import Blueprint, jsonify, request
from auth import token_required
from db import books, get_next_id
from models import Book

books_bp = Blueprint('books', __name__)

@books_bp.route('/', methods=['GET'])
def get_books():
    search_title = request.args.get('title')
    search_author = request.args.get('author')
    page = int(request.args.get('page', 1))
    limit = int(request.args.get('limit', 10))

    filtered_books = books
    if search_title:
        filtered_books = [book for book in books if search_title.lower() in book.title.lower()]
    if search_author:
        filtered_books = [book for book in filtered_books if search_author.lower() in book.author.lower()]

    start = (page - 1) * limit
    end = start + limit
    paginated_books = filtered_books[start:end]

    return jsonify([book.__dict__ for book in paginated_books])

@books_bp.route('/', methods=['POST'])
@token_required
def add_book():
    data = request.json
    new_book = Book(get_next_id(books), data['title'], data['author'], data['published_year'])
    books.append(new_book)
    print(books)
    return jsonify(new_book.__dict__), 201

@books_bp.route('/<int:book_id>', methods=['PUT'])
@token_required
def update_book(book_id):
    data = request.json
    for book in books:
        if book.id == book_id:
            book.title = data.get('title', book.title)
            book.author = data.get('author', book.author)
            book.published_year = data.get('published_year', book.published_year)
            return jsonify(book.__dict__)
    return jsonify({"message": "Book not found"}), 404

@books_bp.route('/<int:book_id>', methods=['DELETE'])
@token_required
def delete_book(book_id):
    global books
    books = [book for book in books if book.id != book_id]
    return jsonify({"message": "Book deleted"})