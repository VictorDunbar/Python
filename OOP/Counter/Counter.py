
from flask import Flask, render_template, redirect, session
app = Flask(__name__)
app.secret_key = 'roctivrabnud'


@app.route('/')
def root_route():
    print session.has_key('count')
    if not session.has_key('count'):
        session['count'] = 1
    else:
        session['count'] += 1
    return render_template("CountIndex.html")


@app.route('/increment', methods=['POST'])
def increment():
    session['count'] =+ 1
    return redirect("/")


@app.route('/reset')
def reset():
    if session.has_key:
        del session['count']
    return redirect("/")

app.run(debug=True)

