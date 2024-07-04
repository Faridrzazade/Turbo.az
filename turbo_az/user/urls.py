from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BrandViewSet, CarModelViewSet, CarModelAutocomplete
from . import views

router = DefaultRouter()
router.register(r'brands', BrandViewSet)
router.register(r'carmodles', CarModelViewSet)

urlpatterns = [
    path('index', views.index, name='create_car'),
    path('', include(router.urls)),
    path('car-model-autocomplete/', CarModelAutocomplete.as_view(), name='car-model-autocomplete')
]
