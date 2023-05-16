from flask import Flask, render_template, jsonify
import os
from markupsafe import escape
from config import config

app = Flask(__name__)

@app.get("/")
def home():
    return render_template('views/home.html')

if __name__ == '__main__':
    app.run(debug=True,port=5050)
