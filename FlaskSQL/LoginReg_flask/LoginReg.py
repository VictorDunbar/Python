from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re
app = Flask(__name__)
mysql = MySQLConnector(app, 'wall')
EMAIL_REGEX = re.compile(r'"^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$"')
app.secret_key = "RabnudrotciV"


def validateEmail(email):
    if len(email) > 7:
        if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", email) != None:
            return True
    return False


def validateName(name):
    if len(name) > 2:
        if re.match("^[a-zA-Z]*$", name) != None:
            return True
    return False


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['POST'])
def login():
    data = {
        'email': request.form['email'],
        'password': request.form['password']
    }
   
    if len(data['email']) < 1 and len(data['password']) < 8:
        LoginError = "Please input a valid email and password to login"
        return render_template('index.html', LoginError=LoginError)
    
    if not validateEmail(data['email']):
        emailLogin = "Please input a valid email"
        return render_template('index.html', emailLogin=emailLogin)
    if len(data['email']) < 1 and not len(data['password']) < 8:
        emailLogin = "Input an email"
        return render_template('index.html', emailLogin=emailLogin)
    if len(data['password']) < 8 and not len(data['email']) < 1:
        passwordLogin = "Input a valid password. 8 char min."
        return render_template('index.html', passwordLogin=passwordLogin)
    
    query = "SELECT id,email,password,first_name from users WHERE email= :email and password= :password"
   
    logins = mysql.query_db(query, data)
    print len(logins)
    if logins:
        session['name'] = logins[0]['first_name']
        session['user_id'] = logins[0]['id']
        return redirect('/wall')
    else:
        LoginError = "Email and Password do not match"
        return render_template('index.html', LoginError=LoginError)

        return render_template('index.html')


@app.route('/register', methods=['POST'])
def register():
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'password': request.form['password'],
        'pw_confirm': request.form['pw_confirm'],
    }
    flag = False
   
    if not validateName(data['first_name']):
        flag = True
        flash("First Name must be letters only and longer than 2 chars")
   
    if not validateName(data['last_name']):
        flag = True
        flash("Last Name must be letters only and longer than 2 chars")
    
    if not validateEmail(data['email']):
        flag = True
        flash("Please input a valid email")
    
    if len(data['password']) < 8:
        flag = True
        flash("Input a valid password. 8 char min.")
    
    if data['pw_confirm'] != data['password']:
        flag = True
        flash("Password does not match")
    
    if flag:
        session['data'] = data
        return redirect('/')
    else:
        
        dup_query = "SELECT id from users WHERE email= :email"
     
        if mysql.query_db(dup_query, data):  
            flash("This email is already in the our system")
            return redirect('/')
        else:
            
            query = "INSERT INTO users (first_name,last_name,email,password) VALUES (:first_name,:last_name,:email,:password)"
            added = mysql.query_db(query, data)
            if added:
                flash("User Added! Please login now.")
            else:
                flash("User not added, but validation passed")
            return redirect('/')



@app.route('/wall', methods=['GET'])
def wall():
    query = 'SELECT users.first_name, users.last_name, messages.message_content, messages.id, messages.created_at FROM messages JOIN users ON messages.user_id=users.id'
    comment_query = 'SELECT comments.users_id, comments.comment_content, comments.message_id, users.first_name, users.last_name FROM comments INNER JOIN users ON users.id=comments.users_id INNER JOIN messages ON messages.id = comments.message_id'
    messages = mysql.query_db(query)
    comments = mysql.query_db(comment_query)
    return render_template('wall.html', messages=messages, comments=comments)


@app.route('/messages', methods=["POST"])
def messages():
    print 'in messages'
    create_message_query = 'INSERT INTO messages (message, created_at, updated_at, user_id) VALUES ( :text, now(), now(), :user_id)'
    message_data = {
        'text' : request.form['message'],
        'user_id' : session['user_id']
    }
    messages = mysql.query_db(create_message_query, message_data)
    return redirect('/wall')

app.run(debug=True)
