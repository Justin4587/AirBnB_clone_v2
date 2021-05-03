#!/usr/bin/python3
"""Wish I had a full Flask"""
from flask import Flask, render_template
from models import storage
from models.state import State
from operator import attrgetter
app = Flask(__name__)


@app.teardown_appcontext
def teardown(self):
    """ hello oh damn is it the one word one """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """doc strings are terrible and """
    states = storage.all('State')
    values = states.values()
    sort_states = sorted(values, key=attrgetter('name'))
    return render_template('7-states_list.html', states=sort_states)

if __name__ == "__main__":
    """ I hate doc strings """
    app.run(host='0.0.0.0', port=5000)
