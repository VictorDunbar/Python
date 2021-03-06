# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Users(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email_address = models.CharField(max_length=255)
    created_at = models.DateTimeField(max_length=45)
    updated_at = models.DateTimeField(max_length=45)

class Books(models.Model):
    name = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    created_at = models.DateTimeField(max_length=45)
    updated_at = models.DateTimeField(max_length=45)
    uploader = models.ForeignKey('Users', related_name='uploaded_books')
    liked_users = models.ManyToManyField('Users', related_name='liked_books')
