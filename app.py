from flask import Flask, request, jsonify, abort
from functools import wraps

app = Flask(__name__)

books = []
members = []

tokens = {"admin": "secrettoken"}

# Utility Functions
def find_book(book_id):
    return next((book for book in books if book['id'] == book_id), None)

def find_member(member_id):
    return next((member for member in members if member['id'] == member_id), None)

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token or token not in tokens.values():
            abort(401)
        return f(*args, **kwargs)
    return decorated

# CRUD Operations for Books
@app.route('/books', methods=['GET'])
@token_required
def get_books():
    title = request.args.get('title')
    author = request.args.get('author')
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 5))

    filtered_books = books
    if title:
        filtered_books = [book for book in filtered_books if title.lower() in book['title'].lower()]
    if author:
        filtered_books = [book for book in filtered_books if author.lower() in book['author'].lower()]

    start = (page - 1) * per_page
    end = start + per_page
    return jsonify(filtered_books[start:end])

@app.route('/books/<int:book_id>', methods=['GET'])
@token_required
def get_book(book_id):
    book = find_book(book_id)
    if not book:
        abort(404)
    return jsonify(book)

@app.route('/books', methods=['POST'])
@token_required
def create_book():
    data = request.get_json()
    if not data or 'id' not in data or 'title' not in data or 'author' not in data:
        abort(400)
    if find_book(data['id']):
        abort(409)
    books.append(data)
    return jsonify(data), 201

@app.route('/books/<int:book_id>', methods=['PUT'])
@token_required
def update_book(book_id):
    book = find_book(book_id)
    if not book:
        abort(404)
    data = request.get_json()
    book.update(data)
    return jsonify(book)

@app.route('/books/<int:book_id>', methods=['DELETE'])
@token_required
def delete_book(book_id):
    book = find_book(book_id)
    if not book:
        abort(404)
    books.remove(book)
    return '', 204

# CRUD Operations for Members
@app.route('/members', methods=['GET'])
@token_required
def get_members():
    return jsonify(members)

@app.route('/members/<int:member_id>', methods=['GET'])
@token_required
def get_member(member_id):
    member = find_member(member_id)
    if not member:
        abort(404)
    return jsonify(member)

@app.route('/members', methods=['POST'])
@token_required
def create_member():
    data = request.get_json()
    if not data or 'id' not in data or 'name' not in data:
        abort(400)
    if find_member(data['id']):
        abort(409)
    members.append(data)
    return jsonify(data), 201

@app.route('/members/<int:member_id>', methods=['PUT'])
@token_required
def update_member(member_id):
    member = find_member(member_id)
    if not member:
        abort(404)
    data = request.get_json()
    member.update(data)
    return jsonify(member)

@app.route('/members/<int:member_id>', methods=['DELETE'])
@token_required
def delete_member(member_id):
    member = find_member(member_id)
    if not member:
        abort(404)
    members.remove(member)
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
