# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cities_light', '0004_auto_20141027_0931'),
    ]

    operations = [
        migrations.CreateModel(
            name='Airport',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(unique=True, max_length=3, verbose_name=b'\xd0\x9a\xd0\xbe\xd0\xb4')),
                ('city', models.ForeignKey(default=b'', to='cities_light.City')),
                ('country', models.ForeignKey(default=b'', to='cities_light.Country')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
