from flask import Flask, request
from datetime import date
from flask import render_template
from werkzeug.utils import redirect

app = Flask(__name__)
comments = []

@app.route("/")
def hello_world():
    today = date.today()
    return render_template('index.html', date=today, comments=comments)

@app.route("/add-comment", methods=['POST'])
def add_comment():
    comment = request.form['comment']
    comments.append(comment)
    return redirect('/')
