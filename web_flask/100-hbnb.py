#!/usr/bin/python3
"""
Script that  starts Flask app
Listens on 0.0.0.0 port 5000
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
from models.city import City
from models.place import Place


app = Flask(__name__)


@app.teardown_appcontext
def teardown_session(self):
    """tear down the sqlalchemy session """
    storage.close()


@app.route('/hbnb', strict_slashes=False)
def hbnb_filters():
    """dynamically display templates"""
    amenities_list = storage.all(Amenity)
    states_list = storage.all(State)
    places_list = storage.all(Place)

    amenities = [amenity for amenity in amenities_list.values()]
    states = [state for state in states_list.values()]
    places = [place for place in places_list.values()]

    return render_template("100-hbnb.html",
                           states=states, amenities=amenities,
                           places=places)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
