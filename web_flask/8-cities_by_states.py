#!/usr/bin/python3
"""Wish I had a full Flask"""
from flask import Flask, render_template
from models import storage
from models.state import State
from operator import attrgetter
app = Flask(__name__)


@app.teardown_appcontext
def teardown(self):
    """ hello """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """doc strings """
    states = storage.all('State')
    values = states.values()
    sort_states = sorted(values, key=attrgetter('name'))
    return render_template('7-states_list.html', states=sort_states)


@app.route('/cities_by_states', strict_slashes=False)
def cities_too():
    """ doc strings """
    states = storage.all('State')
    values = states.values()
    sort_states = sorted(values, key=attrgetter('name'))
    return render_template('8-cities_by_states.html', states=sort_states)


if __name__ == "__main__":
    """ doc strings """    
    app.run(host='0.0.0.0', port=5000)
