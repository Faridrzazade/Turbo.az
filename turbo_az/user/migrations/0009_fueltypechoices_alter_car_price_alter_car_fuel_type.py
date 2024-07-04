# Generated by Django 5.0.6 on 2024-07-02 15:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_alter_car_price_currency'),
    ]

    operations = [
        migrations.CreateModel(
            name='FuelTypeChoices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16)),
            ],
        ),
        migrations.AlterField(
            model_name='car',
            name='price',
            field=models.PositiveIntegerField(verbose_name='Qiymət'),
        ),
        migrations.AlterField(
            model_name='car',
            name='fuel_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.fueltypechoices', verbose_name='Yanacaq novu'),
        ),
    ]
