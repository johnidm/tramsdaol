# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-06 01:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_geographiccoordinate_search_address'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='geographiccoordinate',
            unique_together=set([('lat', 'lng', 'address', 'search_address')]),
        ),
    ]
