from django.urls import path
from . import views

urlpatterns = [
    path('', views.insertar, name='insertar'),
    path('editar/<int:pk>', views.editar, name='editar'),
    path('mostrar/', views.mostrar, name='mostrar'),
    path('eliminar/<int:pk>', views.eliminar, name='eliminar'),
    path('detalle/', views.detalle.as_view(), name='detalle'),
]