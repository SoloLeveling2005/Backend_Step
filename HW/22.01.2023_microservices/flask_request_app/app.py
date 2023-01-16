import json

import psycopg2
from flask import Flask

app = Flask(__name__)


@app.route("/api/get_all_books/")
def get_all_books():
    connection = psycopg2.connect(
        user="postgres",
        password="Solo2005",
        host="127.0.0.1",
        port="5432",
        dbname="microservices",
    )
    cursor = connection.cursor()
    query_string1 = "select * from django_app_books"
    cursor.execute(query_string1)
    records = cursor.fetchall()
    return {
        'data': records,
        'status': 200,
    }

@app.route("/api/get_book/<book_id>")
def get_book(book_id:str):
    book_id = int(book_id)
    connection = psycopg2.connect(
        user="postgres",
        password="Solo2005",
        host="127.0.0.1",
        port="5432",
        dbname="microservices",
    )
    cursor = connection.cursor()
    query_string1 = f"select * from django_app_books WHERE django_app_books.id = {book_id}"
    cursor.execute(query_string1)
    records = cursor.fetchall()
    return {
        'data': records,
        'status': 200,
    }
