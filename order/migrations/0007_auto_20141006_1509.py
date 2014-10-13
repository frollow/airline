# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0006_auto_20141006_1027'),
    ]

    operations = [
        migrations.CreateModel(
            name='Airport',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=3, verbose_name=b'\xd0\x9a\xd0\xbe\xd0\xb4')),
                ('city', models.CharField(max_length=255, verbose_name=b'\xd0\x93\xd0\xbe\xd1\x80\xd0\xbe\xd0\xb4')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='flight',
            name='date_departure',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='date_return',
        ),
        migrations.AddField(
            model_name='flight',
            name='arrival_time',
            field=models.TimeField(default=datetime.time(15, 9, 52, 836760), verbose_name=b'\xd0\x92\xd1\x80\xd0\xb5\xd0\xbc\xd1\x8f \xd0\xbf\xd1\x80\xd0\xb8\xd0\xbb\xd1\x91\xd1\x82\xd0\xb0'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='flight',
            name='departure_time',
            field=models.TimeField(default=datetime.time(15, 9, 52, 836739), verbose_name=b'\xd0\x92\xd1\x80\xd0\xb5\xd0\xbc\xd1\x8f \xd0\xb2\xd1\x8b\xd0\xbb\xd0\xb5\xd1\x82\xd0\xb0'),
            preserve_default=True,
        ),
    ]
