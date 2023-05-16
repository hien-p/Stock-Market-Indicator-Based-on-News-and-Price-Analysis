from flask import Flask
from markupsafe import escape


app = Flask(__name__)

@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'

@app.route('/')
def index():
    return "<p>Hello</p>"
