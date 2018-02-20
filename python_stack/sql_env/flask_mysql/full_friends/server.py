from flask import Flask, render_template, redirect, request, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/friends', methods=['POST'])
def friends():

    return redirect('/')

app.run(debug=True)
