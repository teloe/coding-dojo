from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    name = request.form['name']
    dojo_location = request.form['location']
    favorite_color = request.form['color']
    return render_template('results.html', name=name, location=dojo_location, color=favorite_color)

app.run(debug=True)
