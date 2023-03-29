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
            /states_list:         display HTML and state info from storage;
"""
from models import storage
from flask import Flask, request, render_template
app = Flask(__name__)


@app.route('/states_list/', strict_slashes=False)
def listthem():
    """88888"""
    states = storage.all('State')
    render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def storclo():
    """8 agaain"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
