# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-17 11:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('symptom', '0002_auto_20181017_2031'),
    ]

    operations = [
        migrations.AddField(
            model_name='questions',
            name='question_index',
            field=models.IntegerField(default=0),
        ),
    ]
