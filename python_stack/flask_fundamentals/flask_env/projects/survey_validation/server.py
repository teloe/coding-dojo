from flask import Flask, render_template, request, redirect, flash
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    form = request.form

    errors = []

    if len(request.form['name']) < 0:
        errors.append("Please enter your first name")
    if len(request.form['location']) < 1:
        errors.append("Please enter your last name")
    if len(request.form['color']) < 1:
        errors.append("Please enter your favorite color")

    if len(errors) > 0:
        for error in errors:
            flash(error)

    # name = request.form['name']
    # dojo_location = request.form['location']
    # favorite_color = request.form['color']
    # return render_template('index.html', name=name, location=dojo_location, color=favorite_color)

    return redirect('/')

app.run(debug=True)
