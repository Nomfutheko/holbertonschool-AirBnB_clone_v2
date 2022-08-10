#!/usr/bin/python3
"""Script that starts a Flask web application"""
from models import storage
from models.state import State
from flask import Flask, render_template
app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(self):
    """Method to manage a database connection"""
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def display_cities_by_states():
    """Method to display the cities by states list"""
    states = storage.all(State).values()
    return render_template('8-cities_by_states.html', states=states)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
