#!/usr/bin/python3
"""
Script that  starts Flask app
Listens on 0.0.0.0 port 5000
"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def teardown_session(self):
    """tear down the sqlalchemy session """
    storage.close()


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states(id=None):
    """dynamically display templates"""
    states = storage.all(State)
    list_of_states = [state for state in states.values()]
    if id is None:
        return render_template("7-states_list.html",
                               list_of_states=list_of_states)
    else:
        for state in list_of_states:
            if state.id == id:
                state = state
                return render_template("9-states.html",
                                       state=state)
        return render_template("9-states.html",
                               state=None)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
