# Generated by Django 3.0.3 on 2020-03-11 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxiapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='working_day',
            name='cash_card',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15, verbose_name='Карта'),
        ),
    ]
