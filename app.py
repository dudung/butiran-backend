# flask --app app run --debug --port=5500

from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Python run!"

@app.route("/about")
def about():
    return "This is the About page."

@app.route("/hello/<name>")
def hello(name):
    return f"Hello, {name}!"

@app.route("/search")
def search():
    name = request.args.get("name")
    age = request.args.get("age")
    city = request.args.get("city")
    return f"Name: {name}, Age: {age}, City: {city}"

if __name__ == "__main__":
    app.run(debug=True)
