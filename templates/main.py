from flask import Flask, render_template, redirect, url_for, Response

__winc_id__ = '9263bbfddbeb4a0397de231a1e33240a'
__human_name__ = 'templates'

from flask import Flask, render_template, redirect, url_for, Response

__winc_id__ = '9263bbfddbeb4a0397de231a1e33240a'
__human_name__ = 'templates'

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('/index.html', title='Index')

@app.route('/home/')
def home():
    status_code = Response(status=302)
    return redirect("/")

@app.route('/about/')
def about():
    return render_template('about.html', title='About')

@app.route('/info/')
def info():
    return render_template('info.html', title='Info')

