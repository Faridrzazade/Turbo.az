# Generated by Django 5.0.6 on 2024-08-05 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0023_profile_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(blank=True, max_length=36, null=True),
        ),
    ]
