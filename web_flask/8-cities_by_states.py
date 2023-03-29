#!/usr/bin/python3
"""
script starts Flask web app
    listen on 0.0.0.0, port 5000
    routes: /:                    display "Hello HBNB!"
            /hbnb:                display "HBNB"
            /c/<text>:            display "C" + text (replace "_" with " ")
            /python/<text>:       display "Python" + text (default="is cool")
            /number/<n>:          display "n is a number" only if int
            /number_template/<n>: display HTML page only if n is int
            /number_odd_or_even/<n>: display HTML page; display odd/even info
            /states_list:         display HTML and state info from storage
            /cities_by_states:    display HTML and state, city relations
"""
from models import storage
from models import *
from flask import Flask, render_template
app = Flask(__name__)


@app.teardown_appcontext
def tear_down(self):
    """after each request remove current SQLAlchemy session"""
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)