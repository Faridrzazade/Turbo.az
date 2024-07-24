from .models import Profile
from django.contrib import admin
from .forms import CarForm
from .models import (
    Car, Mileage, MoneyCurrencies, FuelTypeChoices, TransmissionChoices,
    BodyTypeChoices, ColorChoices, MarketChoices, CityChoices,
    SeatCountChoices, OwnerCount, Brand, CarModel, TransmissionType, ImageCar,YearChoices
)

class CarAdmin(admin.ModelAdmin):
    form = CarForm
    list_display = ( 'brand', 'car_models', 'price', 'year', 'mileage')
    search_fields = ('name', 'brand__name', 'car_models__name', 'year', 'price')
    list_filter = ('brand', 'car_models', 'fuel_type', 'transmission')

    
admin.site.register(YearChoices)
admin.site.register(Car, CarAdmin)
admin.site.register(Mileage)
admin.site.register(MoneyCurrencies)
admin.site.register(FuelTypeChoices)
admin.site.register(TransmissionChoices)
admin.site.register(BodyTypeChoices)
admin.site.register(ColorChoices)
admin.site.register(MarketChoices)
admin.site.register(CityChoices)
admin.site.register(SeatCountChoices)
admin.site.register(OwnerCount)
admin.site.register(Brand)
admin.site.register(CarModel)
admin.site.register(TransmissionType)
admin.site.register(ImageCar)



@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio', 'location', 'birth_date')