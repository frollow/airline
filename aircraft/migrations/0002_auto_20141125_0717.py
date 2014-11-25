# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aircraft', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aircraft',
            name='seat_map_picture',
            field=models.ImageField(default=b'', upload_to=b'/Users/MaximSannikov/Desktop/airline/mediaaircraft_images'),
            preserve_default=True,
        ),
    ]
