from django import forms
from .models import Car
from dal import autocomplete

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ('brand', 
                'car_models', 
                'new_bord',
                'mileage',
                'mileage_unit',
                'color',
                'price',
                'price_currency',
                'owner_number',
                'fuel_type',
                'transmission',
                'year',
                'engine_capasity',
                'engine_power',
                'collected_for_which_market',
                'damage_have',
                'painted',
                'for_accident_or_spare_parts',
                'seat_count',
                'credit_available',
                'barter_available',
                'vin_number',
                'additional_info',
                'light_alloy_whells',
                'central_locking',
                'leather_seat',
                'ventilatet_seats',
                'abs_locking',
                'parking_radar',
                'rear_view_camera',
                'xenon_lights',
                'sundroof',
                'air_conditioner',
                'heated_seats',
                'side_curtains',
                'rain_sensor',
                'front_view_image',
                'rear_view_image',
                'interior_view_image',
                'contact_name',
                'city',
                'email',
                'phone_number',

        )
        widgets = {
            'car_models': autocomplete.ModelSelect2(url='car-model-autocomplete', forward=['brand'])
        }