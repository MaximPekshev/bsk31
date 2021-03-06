# Generated by Django 2.2.5 on 2020-02-19 14:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, verbose_name='Имя')),
                ('second_name', models.CharField(max_length=30, verbose_name='Фамилия')),
                ('third_name', models.CharField(blank=True, max_length=30, null=True, verbose_name='Отчество')),
                ('driver_license', models.CharField(blank=True, default='', max_length=15, null=True, verbose_name='Номер В/У')),
                ('car_number', models.CharField(blank=True, default='', max_length=15, null=True, verbose_name='Номер А/М')),
                ('car_model', models.CharField(blank=True, default='', max_length=30, null=True, verbose_name='Марка А/М')),
                ('rate', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=15, null=True, verbose_name='Ставка')),
                ('slug', models.SlugField(blank=True, max_length=10, verbose_name='Url')),
                ('debt', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Долг')),
            ],
            options={
                'verbose_name': 'Водитель',
                'verbose_name_plural': 'Водители',
            },
        ),
        migrations.CreateModel(
            name='Working_day',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Дата рабочего дня')),
                ('rate', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Ставка')),
                ('fuel', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='ГСМ')),
                ('penalties', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Штрафы')),
                ('cash', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Наличные')),
                ('cashless', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Безналичные')),
                ('debt_of_day', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Долг дня')),
                ('slug', models.SlugField(blank=True, max_length=10, verbose_name='Url')),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='taxiapp.Driver')),
            ],
            options={
                'verbose_name': 'Рабочий день',
                'verbose_name_plural': 'Рабочие дни',
            },
        ),
    ]
