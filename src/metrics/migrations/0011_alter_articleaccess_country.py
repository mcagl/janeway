# Generated by Django 3.2.19 on 2023-05-24 15:17

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('metrics', '0010_auto_20230317_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articleaccess',
            name='country',
            field=django_countries.fields.CountryField(blank=True, max_length=2, null=True),
        ),
    ]
