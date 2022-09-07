
from django.shortcuts import render
from app_agenda.models import Clientes, Proveedores, Articulos
from django.http import HttpResponse
from django.template import loader



# Create your views here.

def inicio(request):
    return render(request, "app_agenda/inicio.html")


def clientes(request):
    query = Clientes.objects.all()
    clientes_db = {"clientes": query}
    plantilla = loader.get_template("app_agenda/clientes.html")
    doc = plantilla.render(clientes_db)
    return HttpResponse(doc)

def proveedores(request):
    query = Proveedores.objects.all()
    proveedores_db = {"proveedores": query}
    plantilla = loader.get_template("app_agenda/proveedores.html")
    doc = plantilla.render(proveedores_db)
    return HttpResponse(doc)


def articulos(request):
    query = Articulos.objects.all()
    articulos_db = {"articulos": query}
    plantilla = loader.get_template("app_agenda/articulos.html")
    doc = plantilla.render(articulos_db)
    return HttpResponse(doc)
    

