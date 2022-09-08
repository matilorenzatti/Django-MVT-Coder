from django.urls import path
from app_agenda import views

urlpatterns = [
    path("inicio/", views.inicio, name="inicio"),
    path("clientes/", views.clientes, name="clientes"),
    path("proveedores/", views.proveedores, name="proveedores"),
    path("articulos/", views.articulos, name="articulos"),
    path("crear-cliente/", views.cliente_formulario, name="cliente-formulario"),
    path("busqueda-cliente/", views.busqueda_cliente, name="cliente-buscar"),
    path("cliente-buscado/", views.buscar_cliente, name="cliente-buscado"),
    path("crear-articulo/", views.articulo_formulario, name="articulo-formulario"),
    path("busqueda-articulo/", views.busqueda_articulo, name="articulo-buscar"),
    path("articulo-buscado/", views.buscar_articulo, name="articulo-buscado"),    
]
