#!/usr/bin/python3
"""Wish I had a full Flask"""
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown(self):
    """ hello """
    storage.close()


@app.route('/states_list')
def state_list():
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)
