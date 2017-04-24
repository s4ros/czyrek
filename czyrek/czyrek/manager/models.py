# -*- coding: utf-8 -*-
from __future__ import unicode_literals
####################
# Django imports
from django.utils.encoding import python_2_unicode_compatible
from django.db import models

####################
# Schools Model


@python_2_unicode_compatible
class Schools(models.Model):
    name = models.CharField(max_length=100)
    is_available = models.BooleanField()

    def __str__(self):
        return self.name

####################
# Languages Model


@python_2_unicode_compatible
class Languages(models.Model):
    # nie wiem czy po tym bedzie schools?
    name = models.CharField(max_length=30)
    school_id = models.ForeignKey(Schools)
    is_available = models.BooleanField()

    def __str__(self):
        return self.name

####################
# Subjects Model


@python_2_unicode_compatible
class Subjects(models.Model):
    name = models.CharField(max_length=30)
    wage = models.IntegerField()
    school = models.ForeignKey(Schools)
    is_available = models.BooleanField()

    def __str__(self):
        return self.name

####################
# Candidate Model


@python_2_unicode_compatible
class Candidate(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    city = models.CharField(max_length=100)
    address = models.TextField()
    postalcode = models.CharField(max_length=6)
    voivodeship = models.CharField(max_length=50)
    community = models.CharField(max_length=50)
    phone = models.IntegerField()
    pesel = models.IntegerField()
    birthdate = models.DateField()
    last_school = models.CharField(max_length=100)
    primary_language = models.ForeignKey(Languages, related_name="l1")
    secondary_language = models.ForeignKey(Languages, related_name="l2")
    subject_one = models.ForeignKey(Subjects, related_name="s1")
    subject_two = models.ForeignKey(Subjects, related_name="s2")
    subject_three = models.ForeignKey(Subjects, related_name="s3")
    photo = models.FileField(upload_to='candidates/')

    def __str__(self):
        return self.name + " " + self.surname + " (" + str(self.pesel) + ")"
####################
# Profiles Model


@python_2_unicode_compatible
class Profiles(models.Model):
    name = models.CharField(max_length=30)
    school_id = models.ForeignKey(Schools)
    is_available = models.BooleanField()

    def __str__(self):
        return self.name
