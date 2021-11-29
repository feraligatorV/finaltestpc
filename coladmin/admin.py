from django.contrib import admin
from coladmin.models import Alumno, AlumnoAdmin, Materias, MateriaAdmin

admin.site.register(Alumno, AlumnoAdmin)
admin.site.register(Materias,MateriaAdmin)

