from django.urls import path, re_path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),

    path('accounts/login/', auth_views.LoginView.as_view(template_name='core/login.html'),name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),


    path('hotel/list', views.hotel_list, name='hotel_list'),
    re_path(r'listado/reservas/(?P<dia>[0-9]{2})/(?P<mes>[0-9]{2})/(?P<anio>[0-9]{4})/$', views.listado_reservas_fecha, name='listado_reservas_fecha'),
    path('listado/reservas', views.listado_reservas, name='listado_reservas'),
    path('cliente', views.cliente, name="cliente"),
    path('reservas', views.reservas, name="reservas"),

    path('alta/reservas', views.ReservasCreateView.as_view(), name="reservas_alta"),
    path('alta/listado/reservas', views.ReservasListView.as_view(), name="reservas_listado"),
    path('alta/hotel', views.HotelesCreateView.as_view(), name="hotel_alta"),
    
]