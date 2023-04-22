#!/usr/bin/python3
"""
Script that  starts Flask app
Listens on 0.0.0.0 port 5000
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
import models


app = Flask(__name__)


@app.teardown_appcontext
def teardown_session(self):
    """tear down the sqlalchemy session """
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def states_list():
    """displays all states"""
    states = models.storage.all(State)
    list_of_states = [state for state in states.values()]
    return render_template("8-cities_by_states.html",
                           list_of_states=list_of_states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
