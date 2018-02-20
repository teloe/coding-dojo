from flask import Flask, request, render_template, redirect, session, flash
import re
from mysqlconnection import MySQLConnector
from flask_bcrypt import Bcrypt
app = Flask(__name__)
app.secret_key = "oairhgowHRGOUWH"
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
mysql = MySQLConnector(app, 'log_reg')
bcrypt = Bcrypt(app)


@app.route('/')
def index():
    if 'user_id' in session:
        return redirect('/wall')
    return render_template('index.html')


@app.route('/comments', methods=['post'])
def comments():
    if 'user_id' not in session:
        flash("You can't comment if you aren't logged in")
        return redirect('/')
    data = {
        'comment': request.form['comment'],
        'message_id': request.form['message_id'],
        'user_id': session['user_id'],
    }
    query = """INSERT INTO comments (comment, message_id, user_id, created_at, updated_at)
    VALUES (:comment, :message_id, :user_id, NOW(), NOW())"""
    mysql.query_db(query, data)
    return redirect('/wall')


@app.route('/messages', methods=['post'])
def messages():
    if 'user_id' not in session:
        flash('You must be logged in to do that!')
        return redirect('/')
    data = {
        'message': request.form['message'],
        'user_id': session['user_id']
    }
    query = """INSERT INTO messages (message, user_id, created_at, updated_at) VALUES (:message, :user_id, NOW(), NOW())"""
    mysql.query_db(query, data)
    return redirect('/')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')


@app.route('/wall')
def wall():
    if 'user_id' not in session:
        flash('You must be logged in to do that!')
        return redirect('/')
    users = mysql.query_db("SELECT * FROM users WHERE id = :id", {'id': session['user_id']})
    if not len(users):
        flash("Something went wrong")
        return redirect('/')
    msg_query = """SELECT messages.message, messages.created_at, messages.id, users.first_name, users.last_name FROM messages JOIN users ON messages.user_id = users.id ORDER BY messages.created_at DESC"""
    messages = mysql.query_db(msg_query)

    com_query = """SELECT comments.comment, comments.message_id, comments.created_at, users.first_name, users.last_name
    FROM comments
    JOIN users ON comments.user_id = users.id;"""

    comments = mysql.query_db(com_query)

    return render_template('wall.html', user=users[0], posts = messages, comments=comments)


@app.route('/login', methods=['post'])
def login():
    form = request.form
    if not EMAIL_REGEX.match(form['email']) or len(form['password']) < 8:
        flash('Please enter valid credentials', 'errors')
        return redirect('/')

    data = {
        'email': form['email']
    }

    query = "SELECT * FROM users WHERE email = :email"
    users = mysql.query_db(query, data)

    if len(users):
        user = users[0]
        if not bcrypt.check_password_hash(user['password'], form['password']):
            flash('Account with those credentials could not be found', 'error')
            return redirect('/')
        else:
            pass
            # we got here and we made a success
            #store the user's id in the session
            #redirect to our success page
            session['user_id'] = user['id']
            flash('Login successful', 'success')
            return redirect('/wall')
    else:
        flash('Account with those credentials could not be found', 'error')

    return redirect('/')

@app.route('/register', methods=['post'])
def register():
    form = request.form
    errors = []
    if not len(form['first_name']):
        errors.append('Please enter your first name')
    elif len(form['first_name']) < 2:
        errors.append('Must contain at least 2 characters')
    elif not form['first_name'].isalpha():
        errors.append('Must contain letters only')

    if not len(form['last_name']):
        errors.append('Please enter your last name')
    elif len(form['last_name']) < 2:
        errors.append('Must contain at least 2 characters')
    elif not form['last_name'].isalpha():
        errors.append('Must contain letters only')

    if not len(form['email']):
        errors.append('Please enter your email')
    elif not EMAIL_REGEX.match(form['email']):
        errors.append('Please enter a valid email address')

    if not len(form['password']):
        errors.append('Please enter your password')
    elif len(form['password']) < 8:
        errors.append('Must contain at least 8 characters')
    elif form['password'] != form['password_conf']:
        errors.append('Password must match')


    if len(errors):
        for error in errors:
            flash(error)
    else:
        check_email = mysql.query_db("SELECT email FROM users WHERE email = :email", {'email': form['email']})
        if len(check_email):
            flash("Email account already exists!")
            return redirect('/')

        query = """INSERT INTO users(first_name, last_name, email, password, created_at, updated_at)
        VALUES (:first_name, :last_name, :email, :password, NOW(), NOW())"""
        data = {
            'first_name': form['first_name'],
            'last_name': form['last_name'],
            'email': form['email'],
            'password': bcrypt.generate_password_hash(form['password']),
        }
        mysql.query_db(query, data)

    return redirect('/')

app.run(debug=True)
