# Generated by Django 5.0.4 on 2024-07-27 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_imagecar_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16)),
            ],
        ),
    ]
