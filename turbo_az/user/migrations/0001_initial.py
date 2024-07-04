# Generated by Django 5.0.6 on 2024-07-01 16:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=32, verbose_name='Makra')),
                ('car_model', models.CharField(max_length=32, verbose_name='Model')),
                ('new_bord', models.CharField(max_length=32, verbose_name='Ban novu')),
                ('walk', models.PositiveIntegerField(choices=[('km', 'km'), ('mi', 'mi')], verbose_name='Yuruyus')),
                ('color', models.CharField(max_length=32, verbose_name='Reng')),
                ('price', models.IntegerField(choices=[('₼', 'AZN'), ('$', 'USD'), ('€', 'EUR')], verbose_name='Qiymet')),
                ('owner_number', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '8+')], verbose_name='Necenci sahibisiniz?')),
                ('fuel_type', models.CharField(choices=[('benzin', 'Benzin'), ('dizel', 'Dizel'), ('elektrik', 'Elektrik'), ('hibrid', 'Hibrid')], max_length=32, verbose_name='Yanacaq novu')),
                ('transmission', models.CharField(choices=[('manual', 'Manual'), ('auto', 'Auto')], max_length=32, verbose_name='Surretler qutusu')),
                ('year', models.PositiveIntegerField(verbose_name='il')),
                ('engine_capasity', models.PositiveIntegerField(verbose_name='Mühərrikin həcmi, sm³')),
                ('engine_power', models.PositiveIntegerField(verbose_name='Mühərrikin gücü, a.g.')),
                ('collected_for_which_market', models.CharField(max_length=32, verbose_name='Hansi bazar  ucun yigilib')),
                ('damage_have', models.BooleanField(choices=[(True, 'Active'), (False, 'Inactive')], default=False, verbose_name='Vurugu var')),
                ('colored', models.BooleanField(choices=[(True, 'Active'), (False, 'Inactive')], default=False, verbose_name='Renglenib')),
                ('for_accident_or_spare_parts', models.BooleanField(choices=[(True, 'Active'), (False, 'Inactive')], default=False, verbose_name='Qezali ve ya ehtiyyat hisseler ucun')),
                ('seat_count', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '8+')], verbose_name='Yerlerin sayi')),
                ('credit_available', models.BooleanField(default=False, verbose_name='Kreditle')),
                ('barter_available', models.BooleanField(default=False, verbose_name='Barter mumkundur')),
                ('vin_number', models.CharField(max_length=50, verbose_name='VIN_kod')),
                ('additional_info', models.TextField(max_length=320, verbose_name='Elave melumat')),
            ],
        ),
        migrations.CreateModel(
            name='CarFeatures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
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
                ('car', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='features', to='user.car')),
            ],
        ),
        migrations.CreateModel(
            name='CarImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('front_view_image', models.ImageField(blank=True, null=True, upload_to='cars/', verbose_name='Ön görünüşü')),
                ('rear_view_image', models.ImageField(blank=True, null=True, upload_to='cars/', verbose_name='Arxa görünüşü')),
                ('interior_view_image', models.ImageField(blank=True, null=True, upload_to='cars/', verbose_name='Ön paneli')),
                ('car', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='user.car')),
            ],
        ),
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_name', models.CharField(max_length=100, verbose_name='Adınız')),
                ('city', models.CharField(choices=[('baki', 'Bakı'), ('ganja', 'Gəncə'), ('sumqayit', 'Sumqayıt'), ('mingachevir', 'Mingəçevir'), ('shirvan', 'Şirvan'), ('naftalan', 'Naftalan'), ('shaki', 'Şəki'), ('yevlakh', 'Yevlax'), ('khirdalan', 'Xırdalan'), ('shusha', 'Şuşa'), ('lyankaran', 'Lənkəran'), ('khachmaz', 'Xaçmaz'), ('jalilabad', 'Cəlilabad'), ('goychay', 'Göyçay'), ('goranboy', 'Goranboy'), ('gazakh', 'Qazax'), ('gakh', 'Qax'), ('gobustan', 'Qobustan'), ('agadag', 'Ağdaş'), ('agadara', 'Ağdərə'), ('agadam', 'Ağdam'), ('lerik', 'Lerik')], max_length=100, verbose_name='Şəhər')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='E-mail')),
                ('phone_number', models.CharField(max_length=20, verbose_name='Telefon nömrəsi')),
                ('car', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='contact_info', to='user.car')),
            ],
        ),
    ]
