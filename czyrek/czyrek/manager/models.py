from __future__ import unicode_literals

from django.db import models

class User(models.Model):
    login = models.CharField(max_length=50)
    passwd = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    full_name = models.CharField(max_length=30, blank=False)
    lastlog = models.DateTimeField(auto_now=True,editable=False)
    permissions = models.IntegerField()

    def __str__(self):
        return self.login + " (" + self.email + ")" + " - " + self.full_name

class Schools(models.Model):
    name = models.CharField(max_length=100)
    is_available = models.BooleanField()

class Profiles(models.Model):
    school_id = models.ForeignFey(Schools)
    name = models.CharField(max_length=30)
    is_available = models.BooleanField()

#class Languages(models.Model):

class Subjects(models.Model):
    is_available = models.BooleanField()
    wage = models.IntegerField()