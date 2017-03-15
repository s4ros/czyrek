from __future__ import unicode_literals
####################
## Django imports
from django.db import models

####################
## Schools Model
class Schools(models.Model):
    name = models.CharField(max_length=100)
    is_available = models.BooleanField()

    def __str__(self):
        return self.name

####################
## Languages Model
class Languages(models.Model):
    #nie wiem czy po tym bedzie schools?
    school_id = models.ForeignKey(Schools)
    name = models.CharField(max_length=30)
    is_available = models.BooleanField()

    def __str__(self):
        return self.name

####################
## Subjects Model
class Subjects(models.Model):
    name = models.CharField(max_length=30)
    is_available = models.BooleanField()
    wage = models.IntegerField()

    def __str__(self):
        return self.name

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
    primary_language = models.ManyToManyField(Languages, related_name="l1")
    secondary_language = models.ManyToManyField(Languages,related_name="l2")
    subject_one = models.ManyToManyField(Subjects, related_name="s1")
    subject_two = models.ManyToManyField(Subjects,related_name="s2")
    subject_three = models.ManyToManyField(Subjects,related_name="s3")
    photo = models.CharField(max_length=100)

    def __str__(self):
        return self.name+" "+self.surname+" ("+str(self.pesel)+")"
####################
## Profiles Model
class Profiles(models.Model):
    school_id = models.ForeignKey(Schools)
    name = models.CharField(max_length=30)
    is_available = models.BooleanField()

    def __str__(self):
        return self.name
