from django.contrib import admin
# Register your models here.
from .models import (Car, 
                    Mileage, 
                    MoneyCurrencies, 
                    FuelTypeChoices, 
                    TransmissionChoices, 
                    BodyTypeChoices,
                    ColorChoices,
                    MarketChoices,
                    CityChoices,
                    SeatCountChoices,
                    YearChoices,
                    OwnerCount,
                    Brand,
                    CarModel,
                    TransmissionType

                    
                    
)
from .forms import CarForm


class CarAdmin(admin.ModelAdmin):
    form = CarForm


admin.site.register(Mileage)
admin.site.register(MoneyCurrencies)
admin.site.register(FuelTypeChoices)
admin.site.register(TransmissionChoices)
admin.site.register(BodyTypeChoices)
admin.site.register(ColorChoices)
admin.site.register(MarketChoices)
admin.site.register(CityChoices)
admin.site.register(SeatCountChoices)
admin.site.register(YearChoices)
admin.site.register(OwnerCount)
admin.site.register(Brand)
admin.site.register(CarModel)
admin.site.register(Car, CarAdmin)
admin.site.register(TransmissionType)