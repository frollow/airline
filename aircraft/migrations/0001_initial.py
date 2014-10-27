# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aircraft',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('company', models.CharField(max_length=16)),
                ('model', models.CharField(max_length=16)),
                ('seat_count', models.CharField(max_length=3)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
