from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = 'roctivrabnud'

@app.route('/')
def root_route():
    return render_template("index.html")

@app.route('/results',methods=['POST'])
def results():
    print request.form
    nme = request.form['name']
    loc = request.form['location']
    lang = request.form['language']
    comm = request.form['comments']

    if len(request.form['name']) < 1:
        flash("Name cannot be empty!")
    elif len(request.form['comments']) < 1:
        flash("Comments cannot  be empty!")
    elif len(request.form['comments']) > 120:
        flash("Comments cannot be more than 120 characters!")
    else:
        return render_template("result.html",name = nme, location = loc, language = lang, comments = comm)
    return redirect('/')

@app.route('/',methods=['POST'])
def return_route():
    return redirect("/")
app.run(debug=True)