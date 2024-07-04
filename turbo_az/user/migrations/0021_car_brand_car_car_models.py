# Generated by Django 5.0.6 on 2024-07-03 12:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0020_remove_car_car_model_remove_car_brand_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='brand',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='user.brand', verbose_name='Marka'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='car',
            name='car_models',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='user.carmodel', verbose_name='Model'),
            preserve_default=False,
        ),
    ]
