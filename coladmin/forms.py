from django import forms
from .models import Materias, Alumno
from coladmin import models

class MateriasForm(forms.ModelForm):
    class Meta:
        model= Materias
        fields=('nombremateria','alumno')
    
    def __init__(self, *args, **kwargs):
        super(MateriasForm, self).__init__(*args, **kwargs)
        self.fields["alumno"].widget = forms.widgets.CheckboxSelectMultiple()
        self.fields["alumno"].help_text = "Ingrese los Alumnos de la Materia"
        self.fields["alumno"].queryset = Alumno.objects.all()