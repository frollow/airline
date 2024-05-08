# Generated by Django 5.0.4 on 2024-05-08 17:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("unique_flight", "0002_alter_uniqueflight_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="uniqueflight",
            name="arrival_date",
            field=models.DateField(
                default=datetime.date(1990, 1, 1), verbose_name="Arrival date"
            ),
        ),
        migrations.AlterField(
            model_name="uniqueflight",
            name="arrival_time",
            field=models.TimeField(
                default=datetime.time(0, 0), verbose_name="Arrival time"
            ),
        ),
        migrations.AlterField(
            model_name="uniqueflight",
            name="departure_datetime",
            field=models.DateTimeField(
                default=datetime.datetime(1990, 1, 1, 0, 0),
                verbose_name="Departure date and time",
            ),
        ),
    ]