from django.shortcuts import render
from django.shortcuts import redirect
from AppCoder.models import Curso
from AppCoder.models import Alumno
from AppCoder.models import Profesores
from django.http import HttpResponse
from django.template import loader
from AppCoder.forms import Curso_formulario
from AppCoder.forms import Alumno_formulario
from AppCoder.forms import Profesor_formulario

# Create your views here.

def inicio(request):
    return render( request , "padre.html")




def alta_curso(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        camada = request.POST.get('camada')
        curso = Curso(nombre=nombre, camada=camada)
        curso.save()
        return redirect('cursos')
    return render(request, 'formulario.html')



def ver_cursos(request):
    cursos = Curso.objects.all()
    dicc = {"cursos": cursos}
    plantilla = loader.get_template("cursos.html")
    documento =  plantilla.render(dicc)
    return HttpResponse(documento)





def alumnos(request):
    alumnos = Alumno.objects.all() 
    return render(request, "alumnos.html", {"alumnos": alumnos})


def profesores(request):
    profesores = Profesores.objects.all() 
    return render(request, "profesores.html", {"profesores": profesores})






def curso_formulario(request):
    if request.method == "POST":
        mi_formulario = Curso_formulario( request.POST )
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            curso = Curso( nombre=datos["nombre"] , camada=datos["camada"])
            curso.save()
            return render(request, "formulario.html")
    return render(request, "formulario.html")


def alumno_curso(request):
    if request.method == "POST":
        mi_formulario = Alumno_formulario(request.POST)
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            alumno = Alumno(nombre=datos["nombre"], año=datos["año"])
            alumno.save()
            return HttpResponse("Alumno guardado correctamente.")
    else:
        mi_formulario = Alumno_formulario()
    return render(request, "formularioa.html", {"form": mi_formulario})


def profesores_curso(request):
    if request.method == "POST":
        mi_formulario = Profesor_formulario(request.POST)
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            profesor = Profesores(nombre=datos["nombre"], curos=datos["curso"])
            profesor.save()
            return HttpResponse("Profesor guardado correctamente.")
    else:
        mi_formulario = Profesor_formulario()
    return render(request, "formulariop.html", {"form": mi_formulario})






def buscar_curso(request): #1
    if 'nombre' in request.GET:
        nombre = request.GET['nombre']
        if nombre:
            return redirect('buscar', nombre=nombre)
    return render(request, 'buscar_curso.html')



def buscar_alumno(request):
    if 'nombre' in request.GET:
        nombre = request.GET['nombre']
        if nombre:
            return redirect('al_buscar', nombre=nombre)
    return render(request, 'buscar_alumno.html')


def buscar_profesores(request):
    if 'nombre' in request.GET:
        nombre = request.GET['nombre']
        if nombre:
            return redirect('pr_buscar', nombre=nombre)
    return render(request, 'buscar_profesores.html')






def buscar(request):
    nombre = request.GET.get('nombre')
    if nombre:
        cursos = Curso.objects.filter(nombre__icontains=nombre)
        return render(request, "resultado_busqueda.html", {"cursos": cursos})
    else:
        return HttpResponse("Ingrese el nombre del curso")


    

def al_buscar(request, nombre):
    if nombre:
        alumnos = Alumno.objects.filter(nombre__icontains=nombre)
        return render(request, "resultado_busqueda_al.html", {"alumnos": alumnos})
    else:
        return HttpResponse("Ingrese el nombre del alumno")
    

def pr_buscar(request, nombre):
    if nombre:
        profesores = Profesores.objects.filter(nombre__icontains=nombre)
        return render(request, "resultado_busqueda_pr.html", {"profesores": profesores})
    else:
        return HttpResponse("Ingrese el nombre del profesor")






def elimina_curso(request , id):
    curso = Curso.objects.get(id=id)
    curso.delete()
    curso = Curso.objects.all()
    return render(request , "cursos.html" , {"cursos":curso})


def elimina_alumno(request , id):
    alumno = Alumno.objects.get(id=id)
    alumno.delete()
    return redirect('alumnos')


def elimina_profesor(request , id):
    profesores = Profesores.objects.get(id=id)
    profesores.delete()
    return redirect('profesores')





def editar(request , id):
    curso =  Curso.objects.get(id=id)
    if request.method == "POST":
        mi_formulario = Curso_formulario( request.POST )
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            curso.nombre = datos["nombre"]
            curso.camada = datos["camada"]
            curso.save()
            curso = Curso.objects.all()
            return render(request , "cursos.html" , {"cursos":curso})
    else:
        mi_formulario = Curso_formulario(initial={"nombre":curso.nombre, "camada": curso.camada})
    return render( request, "editar_curso.html" , {"mi_formulario": mi_formulario , "curso":curso})


def editar_alumno(request, id):
    alumno = Alumno.objects.get(id=id)
    if request.method == "POST":
        mi_formulario = Alumno_formulario(request.POST)
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            alumno.nombre = datos["nombre"]
            alumno.año = datos["año"]
            alumno.save()
            return redirect('alumnos')
    else:
        mi_formulario = Alumno_formulario(initial={"nombre": alumno.nombre, "año": alumno.año})
    return render(request, "editar_alumno.html", {"mi_formulario": mi_formulario, "alumno": alumno})


def editar_profesor(request, id):
    profesor = Profesores.objects.get(id=id)
    if request.method == "POST":
        mi_formulario = Profesor_formulario(request.POST)
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            profesor.nombre = datos["nombre"]
            profesor.curos = datos["curso"]
            profesor.save()
            return redirect('profesores')
    else:
        mi_formulario = Profesor_formulario(initial={"nombre": profesor.nombre, "curso": profesor.curos})
    return render(request, "editar_profesores.html", {"mi_formulario": mi_formulario, "profesor": profesor})

