# Generated by Django 3.2.13 on 2022-04-22 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_loancustomer_start_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='loancustomer',
            name='paid',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
