from flask import Flask,request,jsonify
app=Flask(__name__)
books=[]
members=[]


#route to add a new book
@app.route('/books',methods=["POST"])
def add_book():
    data=request.get_json()
    books.append(data)
    return jsonify({'message':'Book added successfully','book':data}), 201

#root to get all books
@app.route('/books',methods=["GET"])
def get_books():
    return jsonify(books), 200

#route to update a book
@app.route('/books/<int:book_id>',methods=["PUT"])
def update_book(book_id):
    data=request.get_json()
    if bookid<len(books):
        books[book_id].update(data)
        return jsonify({'message': 'Book updated successfully!', 'book': books[book_id]}), 200
        return jsonify({'error': 'Book not found'}), 404

# Route to delete a book
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    if book_id < len(books):
        books.pop(book_id)
        return jsonify({'message': 'Book deleted successfully!'}), 200
    return jsonify({'error': 'Book not found'}), 404
@app.route('/books')
def page():
    return "Page is running"

if __name__=="__main__":
    app.run(debug=True)