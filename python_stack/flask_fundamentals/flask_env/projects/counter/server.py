from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'n+4+uy21bmwti+lp&7nk)$q^%hu@7yhb'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/increment', methods=['POST'])
def increment_by_two():
    session['count'] += 2
    return redirect('/')


@app.route('/clear', methods=['POST'])
def clear():
    session['count'] = 0
    return redirect('/')

app.run(debug=True)
