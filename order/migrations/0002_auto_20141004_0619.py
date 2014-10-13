# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='class_of_service',
            field=models.CharField(default=b'E', max_length=1, choices=[(b'F', b'\xd0\x9f\xd0\xb5\xd1\x80\xd0\xb2\xd1\x8b\xd0\xb9'), (b'B', b'\xd0\x91\xd0\xb8\xd0\xb7\xd0\xbd\xd0\xb5\xd1\x81'), (b'E', b'\xd0\xad\xd0\xba\xd0\xbe\xd0\xbd\xd0\xbe\xd0\xbc')]),
        ),
    ]
