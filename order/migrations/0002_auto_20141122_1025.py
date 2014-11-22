# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='class_of_service',
            field=models.CharField(default=b'E', max_length=1, verbose_name=b'Class of service'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='order',
            name='is_registered',
            field=models.BooleanField(default=False, verbose_name=b'Is registered'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='order',
            name='order_hash',
            field=models.CharField(default=b'', max_length=256, verbose_name=b'Hash'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='order',
            name='registration_time',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 22, 10, 25, 37, 422907), verbose_name=b'Flight registration time'),
            preserve_default=True,
        ),
    ]
