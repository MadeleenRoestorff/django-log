from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

# Model view sets
router.register(r'fuellog', views.FuelLogViewSet)
router.register(r'fuellog', views.VehicleLogViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
