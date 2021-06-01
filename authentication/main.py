import os

from flask import Flask, redirect, render_template, request, session, url_for
from helpers import get_users, hash_password

__winc_id__ = '8fd255f5fe5e40dcb1995184eaa26116'
__human_name__ = 'authentication'

app = Flask(__name__)

app.secret_key = os.urandom(16)


@app.route('/')
def index():
    return render_template('/index.html', title='Index')


@app.route('/home/')
def redirect_index():
    return redirect(url_for('index'))



@app.route('/about/')
def about():
    return render_template('about.html', title='About')


@app.route('/lon/')
def lon():
    return render_template('lon.html', title='League of Nations')


@app.route('/login/', methods=['GET', 'POST'])
def login():
    # YOUR SOLUTION HERE
    if request.method == 'GET':
        return render_template('login.html', error=request.args.get('error'))
    elif request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        users = get_users()

        # Check if username in database
        if username in users:
            password_encripted = hash_password(password)
            password_db = users[username]
            
            # Check if password matches
            if password_encripted == password_db:
                session['logged_in'] = username
                print ('Ok')
                return render_template('dashboard.html', title='Dashboard')
            else:
                print ('Nok')
                return redirect(url_for('login', error=True))
        else:
            return redirect(url_for('login', error=True))
    return render_template('login.html', title='Login')

@app.route('/dashboard/')
def dashboard():
    # YOUR SOLUTION HERE
    if 'logged_in' in session:
        print('logged in')
        return render_template('dashboard.html', username = session['logged_in'])
    else:
        print('not logged in')
        return redirect(url_for('login'))

@app.route('/logout/', methods=['GET', 'POST'])
def logout():
    # YOUR SOLUTION HERE
    try:
        session.pop('logged_in')
    except:
        pass
    return redirect(url_for('index'))
