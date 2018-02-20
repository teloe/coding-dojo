from flask import Flask, request, render_template, flash, session, redirect
from mysqlconnection import MySQLConnector
from flask.ext.bcrypt import Bcrypt
import re
app = Flask(__name__)
app.secret_key = "asoirgweio4hrtwg39utihug"
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
mysql = MySQLConnector(app, 'log_reg')
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    form = request.form
    if not EMAIL_REGEX.match(form['email']) or len(form['password']) < 8:
        flash('Please enter valid credentials')
        return redirect

    data = {"email": form['email']}

    query = "SELECT * FROM users WHERE email = :email"
    users = mysql.query_db(query, data)

    print users

    return redirect('/')

@app.route('/register', methods=['POST'])
def register():
    form = request.form
    errors = []
# 1. First Name - letters only, at least 2 characters and that it was submitted
    if not len(form['first_name']):
        errors.append('Please enter your first name')
    elif len(form['first_name']) < 2:
        errors.append('First name must contain at least two characters')
    elif not form['first_name'].isalpha():
        errors.append('First name must be letters only')

# 2. Last Name - letters only, at least 2 characters and that it was submitted
    if not len(form['last_name']):
        errors.append('Please enter your last name')
    elif len(form['last_name']) < 2:
        errors.append('First name must contain at least two characters')
    elif not form['last_name'].isalpha():
        errors.append('First name must be letters only')

# 3. Email - Valid Email format, and that it was submitted
    if not len(form['email']):
        errors.append('Please enter your email')
    elif not EMAIL_REGEX.match(form['email']):
        errors.append('Please enter a valid email address')

# 4. Password - at least 8 characters, and that it was submitted
    if not len(form['password']):
        errors.append('Please enter your password')
    elif len(form['password']) < 8:
        errors.append('Password must contain at least eight characters')

# 5. Password Confirmation - matches password
    elif form['password'] != form['passconf']:
        errors.append('Password must match confirmation field')

    if len(errors):
        for error in errors:
            flash(error)
    else:
        check_email = mysql.query_db("SELECT email FROM users WHERE email = :email", {'email': form['email']})
        if len(check_email):
            flash("Account at email address ({}) already exists".format(form['email']))
            return redirect('/')
        query = """INSERT INTO users (first_name, last_name, email, password, created_at, updated_at)
        VALUES (:first_name, :last_name, :email, :password, NOW(), NOW())"""
        data = {
            'first_name': form['first_name'],
            'last_name': form['last_name'],
            'email': form['email'],
            'password': bcrypt.generate_password_hash(form['password']),
        }
        mysql.query_db(query, data)

    print request.form, errors
    return redirect('/')

app.run(debug=True)
