# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-13 15:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
        ('gr_users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gruser',
            name='books',
            field=models.ManyToManyField(to='books.Book'),
        ),
        migrations.AddField(
            model_name='gruser',
            name='shelves',
            field=models.ManyToManyField(to='books.Shelf'),
        ),
    ]