from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def root_route():
    return render_template("index.html")

@app.route('/Projects')
def projects_route():
    return render_template("Projects.html")

@app.route('/About')
def about_route():
    return render_template("About.html")

app.run(debug=True)