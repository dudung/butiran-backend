# flask --app app run --debug --port=5500

from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "a response from butiran-backend on pythonanywhere"
