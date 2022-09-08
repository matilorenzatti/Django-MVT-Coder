
from django.shortcuts import render
from app_agenda.models import Clientes, Proveedores, Articulos
from django.http import HttpResponse
from django.template import loader
from app_agenda.forms import ClienteFormulario, ProveedorFormulario, ArticuloFormulario



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


def cliente_formulario(request):
    if request.method == "POST":
        formulario_c = ClienteFormulario(request.POST)

        if formulario_c.is_valid():
            data = formulario_c.cleaned_data
            cliente = Clientes(nombre=data["nombre"], apellido=data["apellido"] , mail=data["mail"] , fecha_nacimiento=data["fecha_nacimiento"])
            cliente.save()
            return render(request, "app_agenda/cliente_agregado.html")
    else:
        formulario_c = ClienteFormulario()
    return render(request, "app_agenda/cliente_form.html", {"formulario_c": formulario_c})


def busqueda_cliente(request):
    return render(request, "app_agenda/cliente_busqueda.html")


def buscar_cliente(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        clientes = Clientes.objects.filter(nombre__icontains = nombre)
        return render(request, "app_agenda/clientes.html", {"clientes": clientes})
    else:
        return render(request, "app_agenda/clientes.html", {"clientes": []})


def proveedor_formulario(request):
    if request.method == "POST":
        formulario_p = ProveedorFormulario(request.POST)

        if formulario_p.is_valid():
            data = formulario_p.cleaned_data
            proveedor = Proveedores(nombre=data["nombre"], apellido=data["apellido"] , mail=data["mail"] , telefono=data["telefono"])
            proveedor.save()
            return render(request, "app_agenda/proveedor_agregado.html")
    else:
        formulario_p = ProveedorFormulario()
    return render(request, "app_agenda/proveedor_form.html", {"formulario_p": formulario_p})


def busqueda_proveedor(request):
    return render(request, "app_agenda/proveedor_busqueda.html")


def buscar_proveedor(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        proveedores = Proveedores.objects.filter(nombre__icontains = nombre)
        return render(request, "app_agenda/proveedores.html", {"proveedores": proveedores})
    else:
        return render(request, "app_agenda/proveedores.html", {"proveedores": []})


def articulo_formulario(request):
    if request.method == "POST":
        formulario_a = ArticuloFormulario(request.POST)

        if formulario_a.is_valid():
            data = formulario_a.cleaned_data
            articulo = Articulos(id_articulo=data["id_articulo"], nombre=data["nombre"] , precio=data["precio"])
            articulo.save()
            return render(request, "app_agenda/articulo_agregado.html")
    else:
        formulario_a = ArticuloFormulario()
    return render(request, "app_agenda/articulo_form.html", {"formulario_a": formulario_a})


def busqueda_articulo(request):
    return render(request, "app_agenda/articulo_busqueda.html")


def buscar_articulo(request):
    if request.GET["id_articulo"]:
        id = request.GET["id_articulo"]
        articulos = Articulos.objects.filter(id_articulo__icontains = id)
        return render(request, "app_agenda/articulos.html", {"articulos": articulos})
    else:
        return render(request, "app_agenda/articulos.html", {"articulos": []})