# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-06-25 16:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bugs', '0004_auto_20190624_0745'),
    ]

    operations = [
        migrations.AddField(
            model_name='bug',
            name='comments',
            field=models.CharField(default='', max_length=254),
        ),
        migrations.AlterField(
            model_name='bug',
            name='content',
            field=models.CharField(default='', max_length=254),
        ),
    ]
