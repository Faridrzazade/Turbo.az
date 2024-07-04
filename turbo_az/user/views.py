from django.shortcuts import render #
from user.models import Car #
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import BrandSerializer, CarModelSerializer
from dal import autocomplete
from .models import (
    Brand, 
    CarModel,
    FuelTypeChoices,
    TransmissionChoices,
    BodyTypeChoices,
    ColorChoices,
    MarketChoices,
    CityChoices,
    SeatCountChoices,
    OwnerCount,
    YearChoices,
    Mileage,
    MoneyCurrencies,
    TransmissionType
    
)


class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

    @action(detail=True, methods=['get'])
    def models(self, request, pk=None):
        brand = self.get_object()
        car_models = CarModel.objects.filter(brand=brand)
        serializer = CarModelSerializer(car_models, many=True)
        return Response(serializer.data)

class CarModelViewSet(viewsets.ModelViewSet):
    queryset = CarModel.objects.all()
    serializer_class = CarModelSerializer

class CarModelAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return CarModel.objects.none()
        
        qs = CarModel.objects.all()


        brand_id = self.forwarded.get('brand', None)

        if brand_id:
            qs = qs.filter(brand_id=brand_id)
        
        return qs



# Create your views here.
def index(request):
    cars = Car.objects.all()  
    brands_car = Brand.objects.all()
    models_car = CarModel.objects.all()
    fuel_type  = FuelTypeChoices.objects.all()
    transmission = TransmissionChoices.objects.all()
    body_type = BodyTypeChoices.objects.all()
    color = ColorChoices.objects.all()
    market = MarketChoices.objects.all()
    city = CityChoices.objects.all()
    seat_count = SeatCountChoices.objects.all()
    owner_count = OwnerCount.objects.all()
    year = YearChoices.objects.all()
    milage_car = Mileage.objects.all()
    mony_currenc = MoneyCurrencies.objects.all()
    transmission_type = TransmissionType.objects.all()

    context = {
        'cars': cars,
        'brands_car': brands_car,
        'models_car': models_car,
        'fuel_type': fuel_type,
        'transmission': transmission,
        'body_type': body_type,
        'color': color,
        'market': market,
        'city': city,
        'seat_count': seat_count,
        'owner_count': owner_count,
        'year': year,
        'milage_car': milage_car,
        'mony_currenc': mony_currenc,
        'transmission_type': transmission_type
    }
    return render(request, 'user/create_car.html', context)
