from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.views.generic.base import RedirectView
from .views import BrandViewSet, CarModelViewSet, CarModelAutocomplete
from . import views

router = DefaultRouter()
router.register(r'brands', BrandViewSet)
router.register(r'carmodles', CarModelViewSet)

urlpatterns = [
    path('create_car/', views.create_car, name='create_car'),
    path('edit_car/<int:car_id>/', views.edit_car, name='edit_car'),  # Yeni düzenleme URL'si
    path('api', include(router.urls)),
    path('car-model-autocomplete/', CarModelAutocomplete.as_view(), name='car-model-autocomplete'),
    path('', views.home, name='home'),
    path('salon/', views.salons, name='salons'),
    path('favicon.ico/', RedirectView.as_view(url='/static/favicon.ico')),
    path('like/', views.like_page, name='like_page'),
    path('login-register/', views.login_register, name='login_register'),
    path('login/', views.login_user, name='login_user'),
    path('register/', views.register_user, name='register_user'),
]