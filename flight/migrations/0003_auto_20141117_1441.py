# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0002_auto_20141027_1603'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flight',
            name='arrival_time',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='departure_time',
        ),
        migrations.AddField(
            model_name='flight',
            name='arrival_date',
            field=models.TimeField(default=datetime.datetime(2014, 11, 17, 14, 41, 21, 568741), verbose_name=b'Arrival date'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='flight',
            name='departure_date',
            field=models.TimeField(default=datetime.datetime(2014, 11, 17, 14, 41, 21, 568720), verbose_name=b'Departure date'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='flight',
            name='arrival_city',
            field=models.CharField(max_length=255, verbose_name=b'Arrival city'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='flight',
            name='departure_city',
            field=models.CharField(max_length=255, verbose_name=b'Departure city'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='flight',
            name='flight_number',
            field=models.CharField(max_length=8, verbose_name=b'Flight Number'),
            preserve_default=True,
        ),
    ]
