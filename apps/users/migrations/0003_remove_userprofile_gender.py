# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-07-28 01:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_banner_emailverifyrecord'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='gender',
        ),
    ]
