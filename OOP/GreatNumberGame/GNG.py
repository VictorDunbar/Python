from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'roctivrabnud'


@app.route('/')
def takeAguess():
    session['random'] = (random.randrange(0, 101))
    print session['random']
    return render_template("GNGindex.html")


@app.route('/guess',methods=['POST','GET'])
def Guessed():
    guess = int(request.form['enter_guess'])
    print request.form
    num = session['random']
    
    if guess == None or guess < 0:
        text = 'Good Try...'

    elif num < guess:
        print guess, 'is higher than...', num
        text = 'Too High!'

    elif num > guess:
        print guess, 'is lower than...', num
        text = 'Too Low!'
    
    elif num == guess:
        print 'Win'
        text = 'That is Correct!!'
    return render_template("GNGindex.html", text = text)

@app.route('/play_again',methods=['POST','GET'])
def return_route():
    print 'play again'
    return redirect("/")

app.run(debug=True)
