from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    display_name = models.CharField(max_length=100, blank=True)
    
    def __unicode__(self):
        return u'{l}, {f}'.format(l=self.last_name, f=self.first_name)
        
class Book(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField(max_length=2500, blank=True)
    authors = models.ManyToManyField(Author, blank=True)
    
    def __unicode__(self):
        return self.title
        
class Shelf(models.Model):
    title = models.CharField(max_length=100)
    books = models.ManyToManyField(Book, blank=True)
    
    
    def __unicode__(self):
        return self.title