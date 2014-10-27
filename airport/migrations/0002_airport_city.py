# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('city', '__first__'),
        ('airport', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='airport',
            name='city',
            field=models.ForeignKey(default=b'', to='city.City'),
            preserve_default=True,
        ),
    ]
