# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-03-10 16:18
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('identifiers', '0006_crossrefdeposit'),
    ]

    operations = [
        migrations.AddField(
            model_name='crossrefdeposit',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 10, 16, 18, 15, 765357, tzinfo=utc)),
        ),
    ]
