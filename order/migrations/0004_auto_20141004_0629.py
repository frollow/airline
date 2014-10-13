# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_auto_20141004_0624'),
    ]

    operations = [
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('departure_city', models.CharField(max_length=255)),
                ('arrival_city', models.CharField(max_length=255)),
                ('date_departure', models.DateField(default=datetime.date(2014, 10, 4), verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xb2\xd1\x8b\xd0\xbb\xd0\xb5\xd1\x82\xd0\xb0')),
                ('date_return', models.DateField(default=datetime.date(2014, 10, 11), verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xbf\xd1\x80\xd0\xb8\xd0\xbb\xd1\x91\xd1\x82\xd0\xb0')),
                ('class_of_service', models.CharField(default=b'E', max_length=1, choices=[(b'F', b'\xd0\x9f\xd0\xb5\xd1\x80\xd0\xb2\xd1\x8b\xd0\xb9'), (b'B', b'\xd0\x91\xd0\xb8\xd0\xb7\xd0\xbd\xd0\xb5\xd1\x81'), (b'E', b'\xd0\xad\xd0\xba\xd0\xbe\xd0\xbd\xd0\xbe\xd0\xbc')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='Order',
        ),
    ]
