from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def root_route():
    return render_template("index.html")

@app.route('/ninjas')
def ninja_route():
    return render_template("ninjas.html")

@app.route('/dojos')
def dojo_route():
    return render_template("dojos.html")

app.run(debug=True)