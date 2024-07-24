# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets
from dal import autocomplete
from .forms import CarForm
from .models import (
    Car, Brand, CarModel, FuelTypeChoices, TransmissionChoices,
    BodyTypeChoices, ColorChoices, MarketChoices, CityChoices,
    SeatCountChoices, OwnerCount, YearChoices, Mileage, MoneyCurrencies,
    TransmissionType, ImageCar, Profile
)
from .serializers import BrandSerializer, CarModelSerializer
from django.shortcuts import get_object_or_404

def edit_car(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES, instance=car)
        if form.is_valid():
            form.save()
            return redirect('home') 
    else:
        form = CarForm(instance=car)
    
    return render(request, 'user/edit_car.html', {'form': form, 'car': car})

def register_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        if not username:
            messages.error(request, 'İstifadəçi adı daxil edilməlidir.')
            return render(request, 'user/register_user.html')
        
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Bu istifadəçi adı artıq mövcuddur.')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                profile, created = Profile.objects.get_or_create(user=user)
                if created:
                    profile.save()
                login(request, user)
                return redirect('home')
        else:
            messages.error(request, 'Şifrələr uyğun deyil.')
    
    return render(request, 'user/register_user.html')


def login_user(request):
    if request.method == 'POST':
        print(request.POST)  
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Yanlış istifadəçi adı və ya şifrə.')
    
    return render(request, 'user/login_user.html')


def create_car(request):
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            car = form.save(commit=False)
            car.user = request.user
            car.save()
            return redirect('home')
    else:
        form = CarForm()

    context = {
        'form': form,
        'brands': Brand.objects.all(),
        'models_car': CarModel.objects.all(),
        'fuel_type': FuelTypeChoices.objects.all(),
        'transmission': TransmissionChoices.objects.all(),
        'body_type': BodyTypeChoices.objects.all(),
        'color': ColorChoices.objects.all(),
        'market': MarketChoices.objects.all(),
        'city': CityChoices.objects.all(),
        'seat_count': SeatCountChoices.objects.all(),
        'owner_count': OwnerCount.objects.all(),
        'year': YearChoices.objects.all(),
        'milage_car': Mileage.objects.all(),
        'mony_currenc': MoneyCurrencies.objects.all(),
        'transmission_type': TransmissionType.objects.all(),
        'image_car': ImageCar.objects.all()
    }
    return render(request, 'user/create_car.html', context)


def home(request):
    cars = Car.objects.all()
    brand = request.GET.get('brand')

    if brand:
        cars = cars.filter(brand=brand)

    context = {
        'cars': cars,
        'brands_car': Brand.objects.all(),
        'models_car': CarModel.objects.all(),
        'fuel_type': FuelTypeChoices.objects.all(),
        'transmission': TransmissionChoices.objects.all(),
        'body_type': BodyTypeChoices.objects.all(),
        'color': ColorChoices.objects.all(),
        'market': MarketChoices.objects.all(),
        'city': CityChoices.objects.all(),
        'seat_count': SeatCountChoices.objects.all(),
        'owner_count': OwnerCount.objects.all(),
        'year': YearChoices.objects.all(),
        'milage_car': Mileage.objects.all(),
        'mony_currenc': MoneyCurrencies.objects.all(),
        'transmission_type': TransmissionType.objects.all(),
        'image_car': ImageCar.objects.all()
    }
    return render(request, 'user/home.html', context)


def login_register(request):
    return render(request, 'user/login_register.html')


def salons(request):
    return render(request, 'salons/salons.html')


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


def like_page(request):
    return render(request, 'user/like.html')
