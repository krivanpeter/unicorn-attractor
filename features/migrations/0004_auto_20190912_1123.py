# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-09-12 10:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0003_auto_20190912_1122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feature',
            name='open',
            field=models.CharField(choices=[('OP', 'Opened'), ('DEV', 'Under Development'), ('CL', 'Closed')], default=('OP', 'Opened'), max_length=1),
        ),
    ]
