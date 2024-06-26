# Generated by Django 5.0.4 on 2024-05-08 17:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("flight", "0003_alter_flight_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="flight",
            name="arrival_date_begin",
            field=models.DateField(
                default=datetime.date(1990, 1, 1), verbose_name="Arrival date begin"
            ),
        ),
        migrations.AlterField(
            model_name="flight",
            name="arrival_time",
            field=models.TimeField(
                default=datetime.time(10, 0), verbose_name="Arrival time"
            ),
        ),
        migrations.AlterField(
            model_name="flight",
            name="departure_date_begin",
            field=models.DateField(
                default=datetime.date(1990, 1, 1), verbose_name="Departure date begin"
            ),
        ),
        migrations.AlterField(
            model_name="flight",
            name="departure_time",
            field=models.TimeField(
                default=datetime.time(8, 0), verbose_name="Departure time"
            ),
        ),
    ]
