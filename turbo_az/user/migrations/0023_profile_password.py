# Generated by Django 5.0.6 on 2024-08-05 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0022_remove_profile_bio_remove_profile_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='password',
            field=models.CharField(blank=True, max_length=36, null=True),
        ),
    ]
