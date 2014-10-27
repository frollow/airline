# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('flight_number', models.CharField(max_length=8, verbose_name=b'\xd0\x9d\xd0\xbe\xd0\xbc\xd0\xb5\xd1\x80 \xd1\x80\xd0\xb5\xd0\xb9\xd1\x81\xd0\xb0')),
                ('departure_city', models.CharField(max_length=255, verbose_name=b'\xd0\x9f\xd1\x83\xd0\xbd\xd0\xba\xd1\x82 \xd0\xb2\xd1\x8b\xd0\xbb\xd0\xb5\xd1\x82\xd0\xb0')),
                ('arrival_city', models.CharField(max_length=255, verbose_name=b'\xd0\x9f\xd1\x83\xd0\xbd\xd0\xba\xd1\x82 \xd0\xbf\xd1\x80\xd0\xb8\xd0\xb1\xd1\x8b\xd1\x82\xd0\xb8\xd1\x8f')),
                ('departure_time', models.TimeField(default=datetime.time(11, 16, 35, 394573), verbose_name=b'\xd0\x92\xd1\x80\xd0\xb5\xd0\xbc\xd1\x8f \xd0\xb2\xd1\x8b\xd0\xbb\xd0\xb5\xd1\x82\xd0\xb0')),
                ('arrival_time', models.TimeField(default=datetime.time(11, 16, 35, 394595), verbose_name=b'\xd0\x92\xd1\x80\xd0\xb5\xd0\xbc\xd1\x8f \xd0\xbf\xd1\x80\xd0\xb8\xd0\xbb\xd1\x91\xd1\x82\xd0\xb0')),
                ('class_of_service', models.CharField(default=b'E', max_length=1, choices=[(b'F', b'\xd0\x9f\xd0\xb5\xd1\x80\xd0\xb2\xd1\x8b\xd0\xb9'), (b'B', b'\xd0\x91\xd0\xb8\xd0\xb7\xd0\xbd\xd0\xb5\xd1\x81'), (b'E', b'\xd0\xad\xd0\xba\xd0\xbe\xd0\xbd\xd0\xbe\xd0\xbc')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
