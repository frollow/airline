# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0003_auto_20141122_2336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='arrival_date_begin',
            field=models.DateField(default=datetime.date(2014, 11, 23), verbose_name=b'Arrival date begin'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='flight',
            name='departure_date_begin',
            field=models.DateField(default=datetime.date(2014, 11, 23), verbose_name=b'Departure date begin'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='flight',
            name='price_B',
            field=models.FloatField(default=b'18200', verbose_name=b'Price business class'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='flight',
            name='price_E',
            field=models.FloatField(default=b'11400', verbose_name=b'Price economic class'),
            preserve_default=True,
        ),
    ]
