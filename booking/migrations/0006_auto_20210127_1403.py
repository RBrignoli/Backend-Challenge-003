# Generated by Django 3.0.7 on 2021-01-27 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0005_booking_charge_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='charge_id',
            field=models.CharField(max_length=30, verbose_name='charge'),
        ),
    ]
