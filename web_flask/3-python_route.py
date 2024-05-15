#!/usr/bin/python3
"""
    Sript that starts a Flask web application
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbn():
    """
        function to return Hello HBNB!
    """
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def HBNB():
    """ Return a string"""
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def Display_text(text):
    """display C followed by the value"""
    return "C {}".format(text.replace("-", " "))

@app.route('/python', strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def pythonText(text="is cool"):
    """display Python followed by the value of the text variable"""
    return "Python {}".format(text.replace("_", " "))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
