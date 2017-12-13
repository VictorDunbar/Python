from __future__ import unicode_literals
from django.db import models
import re
NAME_REGEX = re.compile(r"^[-a-zA-Z']+$")
EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$")


class UserManager(models.Manager):
	def regvalidator(self, postData):
		errors = {}
		if len(postData["first"]) < 1:
			errors["first"] = "Must enter a first name."
		elif len(postData["first"]) < 2:
			errors["first"] = "First name must contain at least two characters."
		elif not NAME_REGEX.match(postData["first"]):
			errors["first"] = "First name contains invalid characters."
		if len(postData["last"]) < 1:
			errors["last"] = "Must enter a last name."
		elif len(postData["last"]) < 2:
			errors["last"] = "Last name must contain at least two characters."
		elif not NAME_REGEX.match(postData["last"]):
			errors["last"] = "Last name contains invalid characters."
		if len(postData["email"]) < 1:
			errors["email"] = "Must enter an email address."
		elif not EMAIL_REGEX.match(postData["email"]):
			errors["email"] = "Email address not valid."
		if User.objects.filter(email=postData["email"]):
			errors["email"] = "Email address is already in use."
		if len(postData["pw"]) < 8:
			errors["pw"] = "Password must contain at least eight characters."
		elif not postData["pw"] == postData["conf_pw"]:
			errors["pw"] = "Password and confirmation do not match."
		return errors

	def logvalidator(self, postData):
		errors = {}
		if len(postData["email"]) < 1:
			errors["email"] = "Must enter an email address."
		elif not EMAIL_REGEX.match(postData["email"]):
			errors["email"] = "Email address not valid."
		if len(postData["pw"]) < 8:
			errors["pw"] = "Password must contain at least eight characters."
		return errors


class User(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	password = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = UserManager()
