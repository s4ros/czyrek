from __future__ import unicode_literals

from django.db import models

# Create your models here.
# Create your models here.
class User(models.Model):
    login = models.CharField(max_length=50, blank=False)
    passwd = models.CharField(max_length=100,blank=False)
    email = models.EmailField(max_length=50)
    full_name = models.CharField(max_length=30, blank=False)
    lastlog = models.DateTimeField(auto_now=False,editable=False)
