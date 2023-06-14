from django.urls import path
from . import views

urlpatterns = [
 path('examen/', views.oficinaListView.as_view(), name='oficina'),
 path('examen/<int:pk>', views.oficninaDetailView.as_view(), name='detalle'),
 path('formulario/', views.oficinaCreateView.as_view(), name='formulario'),
path('formularioEmpleado/', views.empleadoCreateView.as_view(), name='formularioEmpleado')
]