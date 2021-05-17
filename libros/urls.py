"""usuarios URL Configuration"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from libros import views

app_name = 'libros'


urlpatterns = [
    path('', views.Admin_Libro.as_view(), name="admin-libro"),
    path('agregar/', views.Agregar_Libro.as_view(), name="agregar-libro"),
    path('listar/', views.Listar_Libro.as_view(), name="listar-libro"),
    path('buscar/', views.Buscar_Libro.as_view(), name="buscar-libro"),
    path('editar/<slug:pk>/', views.Editar_Libro.as_view(), name="editar-libro"),
    path('eliminar/<slug:pk>/', views.Eliminar_Libro.as_view(), name="eliminar-libro"),




]
