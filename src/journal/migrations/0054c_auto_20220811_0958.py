# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2022-08-11 08:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0054b_remove_journal_press_image_override'),
    ]

    operations = [
        migrations.RenameField(
            model_name='journal',
            old_name='press_image_override_temp',
            new_name='press_image_override',
        ),
    ]
