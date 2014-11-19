# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aircraft', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aircraft',
            name='seat_count',
        ),
        migrations.AddField(
            model_name='aircraft',
            name='seat_count_B',
            field=models.CharField(default=0, max_length=3),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='aircraft',
            name='seat_count_E',
            field=models.CharField(default=0, max_length=3),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='aircraft',
            name='seat_count_F',
            field=models.CharField(default=0, max_length=3),
            preserve_default=True,
        ),
    ]
