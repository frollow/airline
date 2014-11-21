# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('registration_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'Flight registration time')),
                ('first_name', models.CharField(default=b'', max_length=255, verbose_name=b'First name')),
                ('last_name', models.CharField(default=b'', max_length=255, verbose_name=b'Last name')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
