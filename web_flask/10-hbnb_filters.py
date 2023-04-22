#!/usr/bin/python3
"""
Script that  starts Flask app
Listens on 0.0.0.0 port 5000
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity


app = Flask(__name__)


@app.teardown_appcontext
def teardown_session(self):
    """tear down the sqlalchemy session """
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """dynamically display templates"""
    amenities_list = storage.all(Amenity)
    states_list = storage.all(State)
    amenities = [amenity for amenity in amenities_list.values()]
    states = [state for state in states_list.values()]
    return render_template("10-hbnb_filters.html",
                           states=states, amenities=amenities)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
