# Generated by Django 3.0.3 on 2020-03-11 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxiapp', '0002_working_day_cash_card'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver',
            name='fuel_card',
            field=models.CharField(blank=True, default='', max_length=15, null=True, verbose_name='Топливная карта'),
        ),
    ]
