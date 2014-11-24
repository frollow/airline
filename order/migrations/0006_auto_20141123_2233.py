# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_auto_20141123_0152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='registration_time',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 23, 22, 33, 27, 861024), verbose_name=b'Flight registration time'),
            preserve_default=True,
        ),
    ]
