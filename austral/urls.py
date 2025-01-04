from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('vehiculos/', views.vehiculos, name='vehiculos'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('login/', views.login, name='login'),
    path('sedan/', views.sedan, name='sedan'),  
    path('suv/', views.suv, name='suv'),  
    path('minivan/', views.minivan, name='minivan'),  
    path('camioneta/', views.camioneta, name='camioneta'),
    path('reservas/<str:tipo_vehiculo>/', views.reservas, name='reservas'),
    path('vehiculo/<str:tipo>/', views.detalle_vehiculo, name='detalle_vehiculo'),
]


