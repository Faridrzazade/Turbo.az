# Generated by Django 5.0.6 on 2024-07-02 14:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_alter_car_brand_alter_car_car_model'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mileage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=3)),
            ],
        ),
        migrations.AlterField(
            model_name='car',
            name='mileage_unit',
            field=models.CharField(default='km', max_length=2),
        ),
        migrations.AlterField(
            model_name='car',
            name='mileage',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.mileage', verbose_name='Yuruyus'),
        ),
    ]
