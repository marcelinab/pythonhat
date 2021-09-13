from flask import Flask
from datetime import date

app = Flask(__name__)

@app.route("/")
def hello_world():
    today = date.today()
    return f"Today's date: {today}"