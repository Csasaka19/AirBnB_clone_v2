#!/usr/bin/python3
"""
Simple flask web app
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """Simple flask message"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """HBNB message"""
    return "HBNB"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
