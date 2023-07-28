from django.urls import path
from .views import index_View, vehiculoforms_view,  menuView, listar_vehiculo,registro_view,logout_view,login_view,tabla_view

urlpatterns = [
    path('', index_View,name='index'),
    path('add/', vehiculoforms_view, name='vehiculoforms'),
    path('menu/', menuView, name='menu'),
    path('login/', login_view, name='login'),
    path('listar/', listar_vehiculo, name='listar'),
    path('registro/', registro_view, name='registro' ),
    path('logout/', logout_view, name='logout'),
    path('listar/', listar_vehiculo, name='listar'),
    path('tabla/', tabla_view, name='tabla'),
]