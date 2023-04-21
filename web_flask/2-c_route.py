#!/usr/bin/python3
"""
Script that  starts Flask app
Listens on 0.0.0.0 port 5000
"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_route():
    """ home route to display hellow HBNB """
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb_route():
    """ HBNB route """
    return "HBNB"


@app.route('/c/<text>')
def c_is_route(text):
    """ display 'C is <text>' """
    return "C {}".format(text.replace("_", " "))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
