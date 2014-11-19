# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('flight_number', models.CharField(max_length=8, verbose_name=b'Flight Number')),
                ('departure_city', models.CharField(max_length=255, verbose_name=b'Departure city')),
                ('arrival_city', models.CharField(max_length=255, verbose_name=b'Arrival city')),
                ('departure_date', models.DateField(verbose_name=b'Departure date')),
                ('arrival_date', models.DateField(verbose_name=b'Arrival date')),
                ('departure_time', models.TimeField(default=b'08:00', verbose_name=b'Departure time')),
                ('arrival_time', models.TimeField(default=b'10:00', verbose_name=b'Arrival time')),
                ('class_of_service', models.CharField(default=b'E', max_length=1, choices=[(b'F', b'\xd0\x9f\xd0\xb5\xd1\x80\xd0\xb2\xd1\x8b\xd0\xb9'), (b'B', b'\xd0\x91\xd0\xb8\xd0\xb7\xd0\xbd\xd0\xb5\xd1\x81'), (b'E', b'\xd0\xad\xd0\xba\xd0\xbe\xd0\xbd\xd0\xbe\xd0\xbc')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
