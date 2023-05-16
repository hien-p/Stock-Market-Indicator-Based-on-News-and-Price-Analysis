from flask import Flask, jsonify
from markupsafe import escape
from read_data import request_candle_chart_data
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

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

@app.route("/test_csv", methods=['GET'])
def test_csv():
    with app.app_context():
        data = request_candle_chart_data()
        return data