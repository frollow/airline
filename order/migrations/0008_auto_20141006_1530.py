# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('cities_light', '0003_auto_20141006_1027'),
        ('order', '0007_auto_20141006_1509'),
    ]

    operations = [
        migrations.AddField(
            model_name='airport',
            name='country',
            field=models.ForeignKey(default=b'', to='cities_light.Country'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='airport',
            name='city',
            field=models.ForeignKey(default=b'', to='cities_light.City'),
        ),
        migrations.AlterField(
            model_name='airport',
            name='code',
            field=models.CharField(unique=True, max_length=3, verbose_name=b'\xd0\x9a\xd0\xbe\xd0\xb4'),
        ),
        migrations.AlterField(
            model_name='flight',
            name='arrival_time',
            field=models.TimeField(default=datetime.time(15, 30, 2, 133856), verbose_name=b'\xd0\x92\xd1\x80\xd0\xb5\xd0\xbc\xd1\x8f \xd0\xbf\xd1\x80\xd0\xb8\xd0\xbb\xd1\x91\xd1\x82\xd0\xb0'),
        ),
        migrations.AlterField(
            model_name='flight',
            name='departure_time',
            field=models.TimeField(default=datetime.time(15, 30, 2, 133835), verbose_name=b'\xd0\x92\xd1\x80\xd0\xb5\xd0\xbc\xd1\x8f \xd0\xb2\xd1\x8b\xd0\xbb\xd0\xb5\xd1\x82\xd0\xb0'),
        ),
    ]
