from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'c4P*RPDJSo+4K7?'

@app.route('/')
def index():
    if not 'count' in session:
        session['count'] = 0
    return render_template('index.html')

@app.route('/process_money', methods=['post'])
def process_money():
    if request.form['building'] == 'farm':
        gold = random.randint(10, 21)
        session['count'] += gold
    elif request.form['building'] == 'cave':
        gold = random.randint(5, 11)
        session['count'] += gold
    elif request.form['building'] == 'house':
        gold = random.randint(2, 6)
        session['count'] += gold
    elif request.form['building'] == 'casino':
        gold = random.randint(0, 51)
        session['count'] += gold
    print "You earned {} gold coins at the {}".format(gold, request.form['building'])

    return redirect('/')

@app.route('/clear', methods=['POST'])
def clear():
    session['count'] = 0

    return redirect('/')


app.run(debug=True)
