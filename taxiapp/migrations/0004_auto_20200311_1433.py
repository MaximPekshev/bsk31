# Generated by Django 3.0.3 on 2020-03-11 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxiapp', '0003_driver_fuel_card'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='rate',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5, null=True, verbose_name='Ставка'),
        ),
    ]
