# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_auto_20141122_1025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='registration_time',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 22, 23, 36, 59, 237917), verbose_name=b'Flight registration time'),
            preserve_default=True,
        ),
    ]
