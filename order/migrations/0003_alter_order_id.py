# Generated by Django 4.2.3 on 2023-07-14 12:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("order", "0002_alter_order_birth_day_alter_order_booking_id_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
