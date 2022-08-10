#!/usr/bin/python3
"""Script that starts a Flask web application"""
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Method to display the welcome text"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """Method to display the welcome text"""
    return 'HBNB'


@app.route('/c/<input>', strict_slashes=False)
def display_c_input(input):
    """Method to display C + the input text"""
    return 'C %s' % input.replace("_", " ")


@app.route('/python', strict_slashes=False)
@app.route('/python/<p_input>', strict_slashes=False)
def display_python_input(p_input='is cool'):
    """Method to display Python + the input text"""
    return 'Python %s' % p_input.replace("_", " ")


@app.route('/number/<int:n>', strict_slashes=False)
def display_number(n):
    """Method to display "is a number" in case of input n being an int"""
    return '%d is a number' % n


@app.route('/number_template/<int:n>', strict_slashes=False)
def display_template(n):
    """Method to display a template"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def display_odd(n):
    """Method to display a template"""
    return render_template('6-number_odd_or_even.html', n=n)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
