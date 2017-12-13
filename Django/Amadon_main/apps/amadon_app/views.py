# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

# Create your views here.


def index(request):
    return render(request, 'amadon_app/index.html')


def buy(request):
    print request.POST['product_id']
    print request.POST['quantity']
    if 'totalnum' not in request.session:
        request.session['totalnum'] = 0
        request.session['totalsum'] = 0
    if request.POST['product_id'] == '101':
        request.session['totalnum'] += int(request.POST['quantity'])
        new_charge = 19.99 * int(request.POST['quantity'])
        request.session['totalsum'] += new_charge
        request.session['charge'] = new_charge
        request.session['item'] = 'Dojo Tshirt'
    if request.POST['product_id'] == '102':
        request.session['totalnum'] += int(request.POST['quantity'])
        new_charge = 29.99 * int(request.POST['quantity'])
        request.session['totalsum'] += new_charge
        request.session['charge'] = new_charge
        request.session['item'] = 'Dojo Sweater'
    if request.POST['product_id'] == '103':
        request.session['totalnum'] += int(request.POST['quantity'])
        new_charge = 4.99 * int(request.POST['quantity'])
        request.session['totalsum'] += new_charge
        request.session['charge'] = new_charge
        request.session['item'] = 'Dojo Cup'
    if request.POST['product_id'] == '104':
        request.session['totalnum'] += int(request.POST['quantity'])
        new_charge = 49.99 * int(request.POST['quantity'])
        request.session['totalsum'] += new_charge
        request.session['charge'] = new_charge
        request.session['item'] = 'Algorithm Book'
    return redirect('/checkout')


def checkout(request):
    return render(request, 'amadon_app/checkout.html')
