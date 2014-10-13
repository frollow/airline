# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_auto_20141004_0703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='arrival_city',
            field=models.CharField(max_length=255, verbose_name=b'\xd0\x9f\xd1\x83\xd0\xbd\xd0\xba\xd1\x82 \xd0\xbf\xd1\x80\xd0\xb8\xd0\xb1\xd1\x8b\xd1\x82\xd0\xb8\xd1\x8f'),
        ),
        migrations.AlterField(
            model_name='flight',
            name='date_departure',
            field=models.DateField(default=datetime.date(2014, 10, 6), verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xb2\xd1\x8b\xd0\xbb\xd0\xb5\xd1\x82\xd0\xb0'),
        ),
        migrations.AlterField(
            model_name='flight',
            name='date_return',
            field=models.DateField(default=datetime.date(2014, 10, 13), verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xbf\xd1\x80\xd0\xb8\xd0\xbb\xd1\x91\xd1\x82\xd0\xb0'),
        ),
        migrations.AlterField(
            model_name='flight',
            name='departure_city',
            field=models.CharField(max_length=255, verbose_name=b'\xd0\x9f\xd1\x83\xd0\xbd\xd0\xba\xd1\x82 \xd0\xb2\xd1\x8b\xd0\xbb\xd0\xb5\xd1\x82\xd0\xb0'),
        ),
        migrations.AlterField(
            model_name='flight',
            name='flight_number',
            field=models.CharField(max_length=8, verbose_name=b'\xd0\x9d\xd0\xbe\xd0\xbc\xd0\xb5\xd1\x80 \xd1\x80\xd0\xb5\xd0\xb9\xd1\x81\xd0\xb0'),
        ),
    ]
