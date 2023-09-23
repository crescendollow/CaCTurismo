from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('hotel/list', views.hotel_list, name='hotel_list'),
    path('usuario/informacion', views.usuario_informacion, name='usuario_informacion'),
]