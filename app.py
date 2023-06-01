
from flask import Flask,request
import sqlite3
app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return 'hello'

@app.route('/books', methods=['POST'])
def insertBook():
    conn = sqlite3.connect('books.sqlite')
    cursor = conn.cursor()
    request_data = request.get_json()

    new_book = {
        "title": request_data['title'],
        "author": request_data['author'],
        "language": request_data['language']
    }
    sql_query = """INSERT INTO books (title, author, language) VALUES (?, ?, ?)"""
    cursor.execute(sql_query, new_book['title'], new_book['author'], new_book['language'])
    conn.commit()
    return new_book,201



if __name__ == '__main__':
    app.run(debug=True, port=5000)