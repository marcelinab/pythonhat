from flask import Flask, request
from datetime import date
from flask import render_template
from werkzeug.utils import redirect
import psycopg2

app = Flask(__name__)
# Connect to your postgres DB
conn = psycopg2.connect("dbname=chat user=postgres password=admin")

@app.route("/")
def hello_world():
    today = date.today()

    # Open a cursor to perform database operations
    cur = conn.cursor()

    # Execute a query
    cur.execute("SELECT * FROM comments")

    # Retrieve query results
    comments = [comment[0] for comment in cur.fetchall()]

    return render_template('index.html', date=today, comments=comments)

@app.route("/add-comment", methods=['POST'])
def add_comment():
    comment = request.form['comment']
    cur = conn.cursor()
    cur.execute("insert into comments values (%s)", [comment])
    return redirect('/')
