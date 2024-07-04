# Generated by Django 5.0.6 on 2024-07-02 15:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_moneycurrencies_alter_car_mileage_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='price_currency',
            field=models.ForeignKey(default='AZN', on_delete=django.db.models.deletion.CASCADE, to='user.moneycurrencies', verbose_name='Valyuta'),
        ),
    ]
