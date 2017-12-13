from flask import Flask, render_template, request, redirect, session, flash
import re
FIRSTLAST_REGEX = re.compile(r'^[a-zA-Z.+_-]+$')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
UPPERDIGIT_REGEX = re.compile(r'^(?=.*[0-9])(?=.*[A-Z]).+$')
app = Flask(__name__)
app.secret_key = 'roctivrabnud'

@app.route('/')
def root_route():
    return render_template("Index.html")

@app.route('/results',methods=['POST'])
def results():
    print request.form
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    password = request.form['password']
    confirm_password = request.form['confirm_password']
    
    if len(first_name) < 1:
        flash("First Name cannot be empty")
    elif not FIRSTLAST_REGEX.match(first_name):
        flash("First Name can only contain letters")

    elif len(last_name) < 1:
        flash("Last Name cannot be empty")
    elif not FIRSTLAST_REGEX.match(last_name):
        flash("Last Name can only contain letters")

    elif not EMAIL_REGEX.match(email):
        flash("Invalid Email Address format")

    elif len(password) < 1:
        flash("Please enter a password")
    elif len(password) < 8:
        flash("Password must be longer than 8 characters")
    elif not UPPERDIGIT_REGEX.match(password):
        flash("Password must contain at least one upper case letter and one digit")

    elif len(confirm_password) < 1:
        flash("Please confirm password")
    elif password != confirm_password:
        flash("Passwords must match")

    if is_valid:
        add_user = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (:first_name, :last_name, :email, :password, NOW(), NOW())"
        user_data = { 'first_name': request.form["fname"],
                    'last_name': request.form["lname"],
                    'email': request.form["email"],
                    'password': request.form["pword"]
        }
        mysql.query_db(add_user, user_data)
        
    else:
        return render_template("index2.html",first_name = first_name, last_name = last_name, email = email, password = password, confirm_password = confirm_password)
    return redirect('/')



@app.route('/',methods=['POST'])
def return_route():
    return redirect("/")
app.run(debug=True)
