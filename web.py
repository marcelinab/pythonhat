from flask import Flask
from datetime import date
from flask import render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    today = date.today()
    return render_template('index.html', name=today)