from __future__ import unicode_literals
import random
from time import gmtime, strftime, localtime
from django.shortcuts import render, HttpResponse, redirect


def index(request):
    if not 'log' in request.session:
        request.session['log'] = []
    if not 'total' in request.session:
        request.session['total'] = 0
    return render(request, 'NinjaGold_app/index.html')


def process(request):
    pay = 0
    color = 'green'
    loc = ""

    now = strftime("%Y-%m-%d %H:%M %p", localtime())

    if request.POST['action'] == "farm":
        pay = random.randint(10, 20)
        request.session['total'] += pay
        loc = "farm"
    elif request.POST['action'] == "cave":
        pay = random.randint(5, 10)
        request.session['total'] += pay
        loc = "cave"
    elif request.POST['action'] == "house":
        pay = random.randint(2, 5)
        request.session['total'] += pay
        loc = "house"
    elif request.POST['action'] == "casino":
        pay = random.randint(-50, 50)
        request.session['total'] += pay
        loc = "casino"

    if pay < 0:
        color = 'red'

    data = {'color': color, 'pay': pay, 'loc': loc, 'now': now}
    temp = request.session['log']
    temp.append(data)
    request.session['log'] = temp

    return redirect('/')


def clear(request):
    request.session['log'] = []
    request.session['total'] = 0
    return redirect('/')
