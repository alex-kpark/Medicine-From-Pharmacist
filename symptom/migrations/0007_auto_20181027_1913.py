# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-27 19:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('symptom', '0006_auto_20181027_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bodypart',
            name='subquestions',
            field=models.CharField(default='QuestioName', max_length=100),
        ),
    ]