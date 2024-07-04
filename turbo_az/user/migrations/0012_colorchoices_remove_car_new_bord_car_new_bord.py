# Generated by Django 5.0.6 on 2024-07-02 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0011_bodytypechoices'),
    ]

    operations = [
        migrations.CreateModel(
            name='ColorChoices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16)),
            ],
        ),
        migrations.RemoveField(
            model_name='car',
            name='new_bord',
        ),
        migrations.AddField(
            model_name='car',
            name='new_bord',
            field=models.ManyToManyField(to='user.bodytypechoices', verbose_name='Ban novu'),
        ),
    ]
