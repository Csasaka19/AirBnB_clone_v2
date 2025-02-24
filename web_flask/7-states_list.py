#!/usr/bin/python3
"""
Simple flask web app using states
"""
from flask import Flask, render_template
from models import storage
from models import *
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Lists states in a HTML file"""
    states = sorted(list(storage.all("State").values()), key=lambda x: x.name)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """Closes the storage of the states"""
    storage.close()
   

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
