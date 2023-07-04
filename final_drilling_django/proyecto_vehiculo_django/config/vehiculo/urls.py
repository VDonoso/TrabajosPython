from django.urls import path
from .views import IndexPageView, vehiculoforms_view, menuView

urlpatterns = [
    path('', IndexPageView.as_view(), name='index'),
    path('vehiculo/add', vehiculoforms_view, name='vehiculoforms' ),
    path('menu/', menuView, name='Menu'),
]