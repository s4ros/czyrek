from __future__ import unicode_literals

from django.db import models

# Create your models here.
# Create your models here.
class User(models.Model):
    email = models.EmailField()
    full_name = models.CharField(max_length=30, blank=False)
    lastlog = models.DateTimeField(auto_now=True)

