from django.urls import path

from . import views

urlpatterns = [
    path('', views.IngreseRut, name='MenuPrincipal'),

    # ex: /encuestas/2/
    path('MenuPrincipal/', views.MenuPrincipal, name='MenuPrincipal'),

    # ex: /encuestas/5/resultados/
   # path('MenuPrincipal', views.MenuPrincipal, name=''),

    # ex: /encuestas/2/
   # path('editar/<int:pregunta_id>/', views.editar_pregunta, name='editar_pregunta'),
]