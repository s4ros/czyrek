from __future__ import unicode_literals
####################
## Django imports
from django.db import models

####################
## Schools Model
class Schools(models.Model):
    name = models.CharField(max_length=100)
    is_available = models.BooleanField()

####################
## Languages Model
class Languages(models.Model):
    #nie wiem czy po tym bedzie schools?
    school_id = models.ForeignKey(Schools)
    name = models.CharField(max_length=30)
    is_available = models.BooleanField()

####################
## Subjects Model
class Subjects(models.Model):
    is_available = models.BooleanField()
    wage = models.IntegerField()

####################
## Candidate Model
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
    secondary_language = models.ForeignKey(Languages,related_name="l2")
    subject_one = models.ForeignKey(Subjects)
    subject_two = models.ForeignKey(Subjects,related_name="s2")
    subject_three = models.ForeignKey(Subjects,related_name="s3")
    photo = models.CharField(max_length=100)
    class Meta:
        unique_together = (("subject_one", "subject_two", "subject_three"),("primary_language","secondary_language"),)
####################
## Profiles Model
class Profiles(models.Model):
    school_id = models.ForeignKey(Schools)
    name = models.CharField(max_length=30)
    is_available = models.BooleanField()
