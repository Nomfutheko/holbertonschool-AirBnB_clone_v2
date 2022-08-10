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


@app.route('/states', strict_slashes=False)
def display_states():
    """Method to display the only the state list"""
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def display_cities_by_states(id):
    """Method to display the cities by states list"""
    states = storage.all(State).values()
    for state in states:
        if state.id == id:
            return render_template('9-states.html', state=state)
    return render_template('9-states.html', state=None)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
