#!/usr/bin/python3
"""Wish I had a full Flask"""
from flask import Flask, render_template
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


@app.route('/number/<int:n>', strict_slashes=False)
def numnums(n):
    """number"""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def numnums_temp(n):
    """numnums"""
    return render_template('5-number.html', neat=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd(n):
    """odd or even"""
    return render_template('6-number_odd_or_even.html', neat=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
