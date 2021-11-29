from django.conf.urls import url
from . import views

urlpatterns = [
    
    url ('materia/nueva/', views.materia_nueva, name='materia_nueva'),
    ]