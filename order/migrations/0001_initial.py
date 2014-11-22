# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('unique_flight', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('registration_time', models.DateTimeField(default=datetime.datetime(2014, 11, 22, 9, 12, 31, 710767), verbose_name=b'Flight registration time')),
                ('is_registered', models.BooleanField(default=False, verbose_name=b'Is registered?')),
                ('first_name', models.CharField(default=b'', max_length=255, verbose_name=b'First name')),
                ('last_name', models.CharField(default=b'', max_length=255, verbose_name=b'Last name')),
                ('document_id', models.CharField(default=b'', max_length=11, verbose_name=b'Document ID')),
                ('birth_day', models.DateField(default=b'1990-01-01', verbose_name=b'Date of birth')),
                ('email', models.EmailField(default=b'', max_length=255, verbose_name=b'Email')),
                ('order_hash', models.CharField(default=b'', max_length=b'256', verbose_name=b'Hash')),
                ('unique_flight', models.ForeignKey(default=b'', verbose_name=b'Unique flight', to='unique_flight.UniqueFlight')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
