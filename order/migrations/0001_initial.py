# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('departure_city', models.CharField(max_length=255)),
                ('arrival_city', models.CharField(max_length=255)),
                ('class_of_service', models.CharField(default=b'E', max_length=1, choices=[(b'F', b'First'), (b'B', b'Business'), (b'E', b'E')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
