# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('airport', '0001_initial'),
        ('flight', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flight',
            name='arrival_city',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='arrival_date',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='departure_city',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='departure_date',
        ),
        migrations.AddField(
            model_name='flight',
            name='arrival_airport',
            field=models.ForeignKey(related_name='arrival_airport', default=b'', verbose_name=b'Arrival airport', to='airport.Airport'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='flight',
            name='arrival_date_begin',
            field=models.DateField(default=datetime.date(2014, 11, 19), verbose_name=b'Arrival date begin'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='flight',
            name='departure_airport',
            field=models.ForeignKey(related_name='departure_airport', default=b'', verbose_name=b'Departure airport', to='airport.Airport'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='flight',
            name='departure_date_begin',
            field=models.DateField(default=datetime.date(2014, 11, 19), verbose_name=b'Departure date begin'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='flight',
            name='repeat_interval',
            field=models.IntegerField(default=1, verbose_name=b'Repeat interval'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='flight',
            name='class_of_service',
            field=models.CharField(default=b'E', max_length=1, choices=[(b'F', b'First'), (b'B', b'Business'), (b'E', b'Economic')]),
            preserve_default=True,
        ),
    ]
