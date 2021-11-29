from django.shortcuts import render
from django.contrib import messages
from .forms import MateriasForm
from coladmin.models import Materias, Encurso

def materia_nueva(request):
    if request.method == "POST":
        formulario = MateriasForm(request.POST)
        if formulario.is_valid():
            materia = Materias.objects.create(nombremateria=formulario.cleaned_data['nombremateria'])
            for alumno_id in request.POST.getlist('alumnos'):
                encurso = Encurso(alumno_id=alumno_id, materia_id = materia.id)
                encurso.save()
            messages.add_message(request, messages.SUCCESS, 'Materia Guardada Exitosamente')
    else:
        formulario = MateriasForm()
    return render(request, 'materia/materia_editar.html', {'formulario': formulario})

