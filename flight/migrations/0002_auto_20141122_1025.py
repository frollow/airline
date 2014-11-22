# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='flight',
            name='price_B',
            field=models.FloatField(default=b'100', verbose_name=b'Price first class'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='flight',
            name='price_E',
            field=models.FloatField(default=b'100', verbose_name=b'Price first class'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='flight',
            name='price_F',
            field=models.FloatField(default=b'100', verbose_name=b'Price first class'),
            preserve_default=True,
        ),
    ]
