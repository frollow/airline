# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='birth_day',
            field=models.DateField(default=datetime.date(2014, 11, 22), verbose_name=b'Date of birth'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='order',
            name='document_id',
            field=models.CharField(default=b'', max_length=11, verbose_name=b'Document ID'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='order',
            name='email',
            field=models.EmailField(default=b'', max_length=255, verbose_name=b'Email'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='order',
            name='is_registered',
            field=models.BooleanField(default=False, verbose_name=b'Is registered?'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='order',
            name='registration_time',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 22, 9, 33, 48, 386308), verbose_name=b'Flight registration time'),
            preserve_default=True,
        ),
    ]
