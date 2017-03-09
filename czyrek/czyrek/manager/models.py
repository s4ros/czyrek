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

class Candidate(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    city = models.CharField(max_length=100)
    address = models.TextField()
    postalcode = models.IntegerField()
    voivodeship = models.CharField(max_length=50)
    community = models.CharField(max_length=50)
    phone = models.IntegerField()
    pesel = models.IntegerField()
    birthdate = models.DateField()
    last_school = models.CharField(max_length=100)
    primary_language = models.ForeignKey(Languages)
    secondary_language = models.ForeignKey(Languages)
    subject_one = models.ForeignKey(Subjects)
    subject_two = models.ForeignKey(Subjects)
    subject_three = = models.ForeignKey(Subjects)
    photo = models.CharField()

class Schools(models.Model):
    name = models.CharField(max_length=100)
    is_available = models.BooleanField()

class Profiles(models.Model):
    school_id = models.ForeignKey(Schools)
    name = models.CharField(max_length=30)
    is_available = models.BooleanField()

class Languages(models.Model):
    #nie wiem czy po tym bedzie schools?
    school_id = models.ForeignKey(Schools)
    name = models.CharField(max_length=30)
    is_available = models.BooleanField()

class Subjects(models.Model):
    is_available = models.BooleanField()
    wage = models.IntegerField()