# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from models import *
from django.contrib import messages

# Create your views here.
# a GET request to /users - calls the index method to display all the users. This will need a template.
def index(request):
    context = {
        "users": User.objects.all()
    }
    return render(request, "index.html")

# GET request to /users/new - calls the new method to display a form allowing users to create a new user. This will need a template.

def new(request):
    return render(request, "new.html")

# GET request /users/<id>/edit - calls the edit method to display a form allowing users to edit an existing user with the given id. This will need a template.

def edit(request, id):
    context = {
        "user": User.objects.get(id=id)
    }
    return render(request, "edit.html", context)

# GET /users/<id> - calls the show method to display the info for a particular user with given id. This will need a template.

def show(request, id):
    context = {
        "user": User.objects.get(id=id)
    }
    return render(request, "show.html", context)


# POST to /users/create - calls the create method to insert a new user record into our database. This POST should be sent from the form on the page /users/new. Have this redirect to /users/<id> once created.

def create(request):
    errors = User.objects.validator(request.POST, "create")
    if len(errors):
            for error in errors.itervalues():
                    messages.error(request, error)
            return redirect("/users/new")
    else:
            new_user = User.objects.create(first_name=request.POST["first_name"], last_name=request.POST["last_name"], email_address=request.POST["email"])
            print new_user
            return redirect("/users/" + str(new_user.id))

# GET /users/<id>/destroy - calls the destroy method to remove a particular user with the given id. Have this redirect back to /users once deleted.

def destroy(request, id):
        User.objects.get(id=int(id)).delete()
        return redirect("/")
    

# POST /users/<id> - calls the update method to process the submitted form sent from /users/<id>/edit. Have this redirect to /users/<id> once updated.


def update(request, id):
        errors = User.objects.validator(request.POST, "update")
        if len(errors):
                for error in errors.itervalues():
                    messages.error(request, error)
                return redirect("/users/" + id + "/edit")
        else:
                User.objects.filter(_id=int(id)).update(first_name=request.POST["first_name"], last_name=request.POST["last_name"], email_address=request.POST["email"])
                return redirect("/users/"+ id)
