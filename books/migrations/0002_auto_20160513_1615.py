# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-13 16:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='description',
            new_name='desc',
        ),
    ]