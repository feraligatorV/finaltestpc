from django.db import models
from django.contrib import admin



class Alumno(models.Model):
    carne= models.CharField(max_length=9)
    nombre= models.CharField(max_length=70)
    apellidos= models.CharField(max_length=70)
    nacimiento= models.DateField();

    def __str__(self):
        return self.carne

class Materias(models.Model):
    nombremateria= models.CharField(max_length=100)
    alumno    = models.ManyToManyField(Alumno, through='Encurso')

    def __str__(self):
        return self.nombremateria

class Encurso (models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    materia = models.ForeignKey(Materias, on_delete=models.CASCADE)

class EncursoInLine(admin.TabularInline):
    model = Encurso
    extra=1

class AlumnoAdmin(admin.ModelAdmin):
    inlines= (EncursoInLine),

class MateriaAdmin(admin.ModelAdmin):
    inlines= (EncursoInLine),

