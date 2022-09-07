from django.urls import path
from app_agenda import views

urlpatterns = [
    path("inicio/", views.inicio, name="inicio"),
    path("clientes/", views.clientes, name="clientes"),
    path("proveedores/", views.proveedores, name="proveedores"),
    path("articulos/", views.articulos, name="articulos"),
    
]