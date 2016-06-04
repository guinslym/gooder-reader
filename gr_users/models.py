from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User
from books.models import *

# Create your models here.
#GR - gooder-reader
class GRUser(models.Model):
    first_name = models.TextField(max_length=100)
    last_name = models.TextField(max_length=100)
    user = models.ForeignKey(User)
    shelves = models.ManyToManyField(Shelf)
    books = models.ManyToManyField(Book)


    def __unicode__(self):
        return u'{l}, {f}'.format(l=self.last_name, f=self.first_name)
