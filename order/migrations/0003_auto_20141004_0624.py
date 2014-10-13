# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_auto_20141004_0619'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='date_departure',
            field=models.DateField(default=datetime.date(2014, 10, 4), verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xb2\xd1\x8b\xd0\xbb\xd0\xb5\xd1\x82\xd0\xb0'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='order',
            name='date_return',
            field=models.DateField(default=datetime.date(2014, 10, 11), verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xbf\xd1\x80\xd0\xb8\xd0\xbb\xd1\x91\xd1\x82\xd0\xb0'),
            preserve_default=True,
        ),
    ]
