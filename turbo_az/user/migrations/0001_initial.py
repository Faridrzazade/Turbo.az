# Generated by Django 5.0.4 on 2024-07-23 13:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BodyTypeChoices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='CityChoices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='ColorChoices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='FuelTypeChoices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='MarketChoices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Mileage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='MoneyCurrencies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='OwnerCount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=36)),
            ],
        ),
        migrations.CreateModel(
            name='SeatCountChoices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='TransmissionChoices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='TransmissionType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='YearChoices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.brand')),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mileage', models.PositiveIntegerField(verbose_name='Yuruyus')),
                ('price', models.PositiveIntegerField(verbose_name='Qiymət')),
                ('engine_capasity', models.PositiveIntegerField(verbose_name='Mühərrikin həcmi, sm³')),
                ('engine_power', models.PositiveIntegerField(verbose_name='Mühərrikin gücü, a.g.')),
                ('damage_have', models.BooleanField(default=False, verbose_name='Vurugu var')),
                ('painted', models.BooleanField(default=False, verbose_name='Renglenib')),
                ('for_accident_or_spare_parts', models.BooleanField(default=False, verbose_name='Qezali ve ya ehtiyyat hisseler ucun')),
                ('credit_available', models.BooleanField(default=False, verbose_name='Kreditle')),
                ('barter_available', models.BooleanField(default=False, verbose_name='Barter mumkundur')),
                ('vin_number', models.CharField(max_length=17, verbose_name='VIN_kod')),
                ('additional_info', models.TextField(max_length=320, verbose_name='Elave melumat')),
                ('light_alloy_whells', models.BooleanField(default=False, verbose_name='Yüngül lehimli disklər')),
                ('central_locking', models.BooleanField(default=False, verbose_name='Mərkəzi qapanma')),
                ('leather_seat', models.BooleanField(default=False, verbose_name='Dəri salon')),
                ('ventilatet_seats', models.BooleanField(default=False, verbose_name='Oturacaqların ventilyasiyası')),
                ('abs_locking', models.BooleanField(default=False, verbose_name='ABS')),
                ('parking_radar', models.BooleanField(default=False, verbose_name='Park radarı')),
                ('rear_view_camera', models.BooleanField(default=False, verbose_name='Arxa görüntü kamerası')),
                ('xenon_lights', models.BooleanField(default=False, verbose_name='Ksenon lampalar')),
                ('sundroof', models.BooleanField(default=False, verbose_name='Lyuk')),
                ('air_conditioner', models.BooleanField(default=False, verbose_name='Kondisioner')),
                ('heated_seats', models.BooleanField(default=False, verbose_name='Oturacaqların isidilməsi')),
                ('side_curtains', models.BooleanField(default=False, verbose_name='Yan pərdələr')),
                ('rain_sensor', models.BooleanField(default=False, verbose_name='Yağış sensoru')),
                ('front_view_image', models.ImageField(blank=True, null=True, upload_to='user/img_cars', verbose_name='Ön görünüşü')),
                ('rear_view_image', models.ImageField(blank=True, null=True, upload_to='user/img_cars', verbose_name='Arxa görünüşü')),
                ('interior_view_image', models.ImageField(blank=True, null=True, upload_to='user/img_cars', verbose_name='Ön paneli')),
                ('contact_name', models.CharField(default=None, max_length=100, verbose_name='Adınız')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='E-mail')),
                ('phone_number', models.CharField(max_length=20, verbose_name='Telefon nömrəsi')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.brand', verbose_name='Marka')),
                ('new_bord', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.bodytypechoices', verbose_name='Ban novu')),
                ('car_models', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.carmodel', verbose_name='Model')),
                ('city', models.ForeignKey(default='Bakı', on_delete=django.db.models.deletion.CASCADE, to='user.citychoices', verbose_name='Şəhər')),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.colorchoices', verbose_name='Reng')),
                ('fuel_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.fueltypechoices', verbose_name='Yanacaq novu')),
                ('collected_for_which_market', models.ForeignKey(default='Bakı', on_delete=django.db.models.deletion.CASCADE, to='user.marketchoices', verbose_name='Hansi bazar ucun yigilib')),
                ('mileage_unit', models.ForeignKey(default='km', on_delete=django.db.models.deletion.CASCADE, to='user.mileage')),
                ('price_currency', models.ForeignKey(default='AZN', on_delete=django.db.models.deletion.CASCADE, to='user.moneycurrencies', verbose_name='Valyuta')),
                ('owner_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.ownercount', verbose_name='Necenci sahibisiniz?')),
                ('seat_count', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.seatcountchoices', verbose_name='Yerlerin sayi')),
                ('transmission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.transmissionchoices', verbose_name='Surretler qutusu')),
                ('transmission_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.transmissiontype', verbose_name='Ötürücü')),
                ('year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.yearchoices', verbose_name='il')),
            ],
        ),
        migrations.CreateModel(
            name='ImageCar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.car', verbose_name='Avtomobil')),
            ],
            options={
                'verbose_name': 'Avtomobil Şəkili',
                'verbose_name_plural': 'Avtomobil Şəkilləri',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, max_length=500)),
                ('location', models.CharField(blank=True, max_length=30)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
