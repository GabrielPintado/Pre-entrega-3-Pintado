from django.urls import path
from . import views
urlpatterns = [
    path("", views.inicio , name="home"),
    path("ver_cursos", views.ver_cursos, name="cursos"),
    #path("alta_curso/<nombre>", views.alta_curso),
    path("alumnos", views.alumnos , name="alumnos"),
    path("profesores", views.profesores , name="profesores"),

    path("alta_curso", views.alta_curso, name="alta_curso"),
    path("alumno_curso", views.alumno_curso , name="alumno_curso"),
    path("profesores_curso", views.profesores_curso , name="profesores_curso"),

    #path("profesores_curso", views.profesores_formulario),
    path("buscar_cursos", views.buscar_curso, name="buscar_curso"), #1
    path("buscar_alumno", views.buscar_alumno, name="buscar_alumno"),
    path("buscar_profesores", views.buscar_profesores, name="buscar_profesores"),


    path("buscar/", views.buscar, name="buscar"),
    path("al_buscar/<str:nombre>", views.al_buscar, name="al_buscar"),
    path("pr_buscar/<str:nombre>", views.pr_buscar, name="pr_buscar"),


    path("elimina_curso/<int:id>" , views.elimina_curso , name="elimina_curso"),
    path("elimina_alumno/<int:id>" , views.elimina_alumno , name="elimina_alumno"),
    path("elimina_profesor/<int:id>" , views.elimina_profesor , name="elimina_profesor"),

    path("editar_curso/<int:id>" , views.editar , name="editar_curso"),
    path("editar_alumno/<int:id>" , views.editar_alumno , name="editar_alumno"),
    path("editar_profesor/<int:id>" , views.editar_profesor , name="editar_profesor")
]