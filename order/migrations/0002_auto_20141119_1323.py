# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='registration_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'Registration time'),
            preserve_default=True,
        ),
    ]
