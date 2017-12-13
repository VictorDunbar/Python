from flask import Flask, render_template, redirect, request, session, flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = 'ThisIsASecret!'


@app.route('/', methods=['GET'])
def index():
  return render_template('BVindex.html')


@app.route('/process', methods=['Post'])
def submit():
    if len(request.form['email']) < 1:
          flash("Email cannot be blank!")
    else:
          flash("Success!")
  
    return redirect('/')


app.run(debug=True)
