# Generated by Django 5.0.6 on 2024-07-02 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0013_alter_car_color_remove_car_new_bord_car_new_bord'),
    ]

    operations = [
        migrations.CreateModel(
            name='MarketChoices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16)),
            ],
        ),
    ]
