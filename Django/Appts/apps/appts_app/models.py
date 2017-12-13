from __future__ import unicode_literals
from django.db import models


class Appointments(models.Model):
    start_time = models.TimeField()
    start_date = models.DateField()
    task = models.CharField(max_length=155)
    status = models.CharField(max_length=15, default="Pending")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey("logreg_app.User", related_name="creator")
    # users_join = models.ManyToManyField()
