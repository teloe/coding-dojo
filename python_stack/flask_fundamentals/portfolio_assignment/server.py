from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_tem plate('index.html')

@app.route('/projects')
def projects():
    my_projects = ['project1', 'project2', 'project3', 'project4']
    return render_template('projects.html', projects=my_projects)

@app.route('/about')
def about():
    return render_template('about.html')

app.run(debug=True)
