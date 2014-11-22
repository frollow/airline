# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='arrival_date_begin',
            field=models.DateField(default=datetime.date(2014, 11, 22), verbose_name=b'Arrival date begin'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='flight',
            name='departure_date_begin',
            field=models.DateField(default=datetime.date(2014, 11, 22), verbose_name=b'Departure date begin'),
            preserve_default=True,
        ),
    ]
