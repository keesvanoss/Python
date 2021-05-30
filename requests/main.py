__winc_id__ = 'cc1b724762854e85a8defa04287f708b'
__human_name__ = 'requests'

from flask import Flask

app = Flask(__name__)

# Handle no parameters

@app.route('/', methods=['GET'])
def index():
    return '<p>Home, sweet home.</p>'

# Handle only greet

@app.route('/greet/')
def greet1():
    return f'<h1>Hello, world!</h1>'

# Handle greet with name

@app.route('/greet/<name>')
def greet(name):
    return f'<h1>Hello, {name}!</h1>'
