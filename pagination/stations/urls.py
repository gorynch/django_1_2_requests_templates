from django.urls import path

# from . views import index, bus_stations
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('bus_stations/', views.bus_stations, name='bus_stations'),
    path('pagi/', views.pagi),
]
