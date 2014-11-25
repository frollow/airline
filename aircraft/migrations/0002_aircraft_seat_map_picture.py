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
            name='seat_map_picture',
            field=models.FileField(default=b'', upload_to=b''),
            preserve_default=True,
        ),
    ]
