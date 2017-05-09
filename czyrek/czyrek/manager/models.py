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
    shortcut = models.CharField(max_length=5)
    is_available = models.BooleanField()

    def __str__(self):
        return "{} ({})".format(self.name, self.shortcut)

####################
# Languages Model
@python_2_unicode_compatible
class Languages(models.Model):
    BEGINNER = u"P"
    ADVANCED = u"Z"
    LANG_LEVELS = (
        (BEGINNER, u"początkujący"),
        (ADVANCED, u"zaawansowany"),
    )
    name = models.CharField(max_length=30)
    shortcut = models.CharField(max_length=5)
    level = models.CharField(max_length=20, choices=LANG_LEVELS, default=BEGINNER)
    is_available = models.BooleanField()

    def __str__(self):
        # return "{} - {}".format(self.name, self.school_id.name)
        return "{} ({})".format(self.name, self.shortcut)

####################
# Subjects Model
@python_2_unicode_compatible
class Subjects(models.Model):
    name = models.CharField(max_length=30)
    shortcut = models.CharField(max_length=5)
    wage = models.IntegerField()
    is_available = models.BooleanField()

    def __str__(self):
        # return "{} - {}".format(self.name, self.school.name)
        return "{} ({})".format(self.name, self.shortcut)

####################
# Profiles Model
@python_2_unicode_compatible
class Profiles(models.Model):
    name = models.CharField(max_length=30)
    shortcut = models.CharField(max_length=10)
    school_id = models.ForeignKey(Schools)
    is_available = models.BooleanField()

    def __str__(self):
        return "{} - {}".format(self.name, self.school_id.name)


####################
# Candidate Model
@python_2_unicode_compatible
class Candidate(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    phone = models.IntegerField()
    pesel = models.IntegerField()
    birthdate = models.DateField()
    last_school = models.CharField(max_length=100)
    #
    primary_school = models.ForeignKey(Profiles, related_name="p1")
    secondary_school = models.ForeignKey(Profiles, related_name="p2")
    third_school = models.ForeignKey(Profiles, related_name="p3")
    #
    primary_language = models.ForeignKey(Languages, related_name="l1")
    secondary_language = models.ForeignKey(Languages, related_name="l2")
    #
    subject_one = models.ForeignKey(Subjects, related_name="s1")
    subject_two = models.ForeignKey(Subjects, related_name="s2")
    subject_three = models.ForeignKey(Subjects, related_name="s3")

    photo = models.FileField(upload_to='candidates/')
    active_school = models.ForeignKey(Profiles, related_name='active_school')

    def __str__(self):
        return self.name + " " + self.surname + " (" + str(self.pesel) + ")"
