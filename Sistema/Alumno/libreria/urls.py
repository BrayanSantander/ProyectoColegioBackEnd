from django.urls import path
from . import views



urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('estudiante', views.estudiantes, name='estudiante'),
    path('estudiante/crear', views.crear, name='crear'),
    path('estudiante/editar', views.editar, name='editar'),
    path('eliminar/<int:id>', views.eliminar, name='eliminar'),
    path('estudiante/editar/<int:id>', views.editar, name='editar'),

]


