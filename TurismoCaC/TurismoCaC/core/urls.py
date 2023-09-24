from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('hotel/list', views.hotel_list, name='hotel_list'),
    re_path(r'listado/reservas/(?P<dia>[0-9]{2})/(?P<mes>[0-9]{2})/(?P<anio>[0-9]{4})/$', views.listado_reservas, name='listado_reservas'),
    path('listado/reservas', views.listado_reservas, name='listado_reservas')

]