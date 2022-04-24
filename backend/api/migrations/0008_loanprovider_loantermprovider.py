# Generated by Django 3.2.13 on 2022-04-23 02:30

import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_loancustomer_paid'),
    ]

    operations = [
        migrations.CreateModel(
            name='LoanProvider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('value', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('paid', models.PositiveIntegerField(default=0)),
                ('accepted', models.BooleanField(default=False)),
                ('start_date', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('term_id', models.PositiveIntegerField()),
                ('user_id', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='LoanTermProvider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('min', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('max', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('duration', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(120)])),
                ('interest', models.FloatField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
            ],
        ),
    ]
