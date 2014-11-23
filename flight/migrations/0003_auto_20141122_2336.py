# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0002_auto_20141122_1025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='price_B',
            field=models.FloatField(default=b'18200', verbose_name=b'Price first class'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='flight',
            name='price_E',
            field=models.FloatField(default=b'11400', verbose_name=b'Price first class'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='flight',
            name='price_F',
            field=models.FloatField(default=b'22500', verbose_name=b'Price first class'),
            preserve_default=True,
        ),
    ]
