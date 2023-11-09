from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import alumno
from .forms import AlumnoForm


def inicio(request):
    return render(request, "paginas/inicio.html")
def nosotros(request):
    return render(request, "paginas/nosotros.html")


def estudiantes(request):
    estudiantes = alumno.objects.all()
    return render(request, "estudiante/index.html", {"estudiantes":estudiantes})


def crear(request):
    formulario = AlumnoForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect("estudiante")
    return render (request, "estudiante/crear.html", {"formulario":formulario})

def editar(request,id):
    estudiantes = alumno.objects.get(id=id)
    formulario = AlumnoForm(request.POST or None, request.FILES or None, instance=estudiantes)
    if formulario.is_valid()and request.POST:
        formulario.save()
        return redirect("estudiante")
    return render (request, "estudiante/editar.html", {"formulario":formulario})


def eliminar(request,id):
    estudiantes = alumno.objects.get(id=id)
    estudiantes.delete()
    return redirect("estudiante")

