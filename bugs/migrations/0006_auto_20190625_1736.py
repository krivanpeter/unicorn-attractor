# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-06-25 16:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bugs', '0005_auto_20190625_1734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bug',
            name='comments',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='bug',
            name='content',
            field=models.TextField(),
        ),
    ]
