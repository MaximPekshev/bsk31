# Generated by Django 3.0.4 on 2020-03-27 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxiapp', '0010_cashbox'),
    ]

    operations = [
        migrations.CreateModel(
            name='CashboxDbt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('debt', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Остаток в кассе')),
            ],
        ),
    ]