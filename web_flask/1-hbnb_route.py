#!/usr/bin/python3
"""
script starts Flask web application and defines route '/'
"""

from flask import Flask
app = Flask(__name__)


# decorator turns a python function into a Flask view function
@app.route('/', strict_slashes=False)
def hello():
    """
    function responds to web requests to the main URL
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    defining behavior for /hbnb url
    """
    return 'HBNB'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
