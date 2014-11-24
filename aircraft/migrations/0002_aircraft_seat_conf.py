# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aircraft', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='aircraft',
            name='seat_conf',
            field=models.CharField(default=0, max_length=10000),
            preserve_default=True,
        ),
    ]
