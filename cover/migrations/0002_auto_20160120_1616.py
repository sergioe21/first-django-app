# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-20 16:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cover', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='address',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='cellphone',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='person',
            name='profession',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
