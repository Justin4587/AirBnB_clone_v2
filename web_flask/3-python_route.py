#!/usr/bin/python3
"""Wish I had a full Flask"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ hello """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ no way this is it"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """ hello """
    return "C " + text.replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>')
def neat(text='is cool'):
    """ hello """
    return "Python " + text.replace('_', ' ')

    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
