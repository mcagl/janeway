# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-06-14 10:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0002_reviewformelement_default_visibility'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewassignment',
            name='review_type',
            field=models.CharField(choices=[('traditional', 'Traditional')], default='traditional', help_text='Currently only traditional, form based, review is available.', max_length=20),
        ),
        migrations.AlterField(
            model_name='reviewassignment',
            name='visibility',
            field=models.CharField(choices=[('open', 'Open'), ('blind', 'Single Anonymous'), ('double-blind', 'Double Anonymous')], default='double-blind', max_length=20, verbose_name="Anonymity"),
        ),
        migrations.AlterField(
            model_name='reviewformelement',
            name='default_visibility',
            field=models.BooleanField(default=True, help_text='If true, this setting will be available to the author automatically, if false it willbe hidden to the author by default.'),
        ),
    ]
