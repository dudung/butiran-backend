# flask --app app run --debug --port=5500

from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This enables CORS for all routes

@app.route("/")
def home():
    return "a response from butiran-backend on pythonanywhere"
