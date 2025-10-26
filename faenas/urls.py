from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_faenas, name='lista_faenas'),
    path('faenas/crear/', views.crear_faena, name='crear_faena'),
    path('faenas/<int:pk>/', views.detalle_faena, name='detalle_faena'),
    path('faenas/<int:pk>/editar/', views.editar_faena, name='editar_faena'),
    path('faenas/<int:pk>/eliminar/', views.eliminar_faena, name='eliminar_faena'),
    path('predio/', views.seleccionar_predio, name='seleccionar_predio'),
    path('logout/', views.user_logout, name='logout'),
]
