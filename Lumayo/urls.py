"""Lumayo URL Configuration"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from LumayoApp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/', views.Home, name="inicio"),
    path('admin-perfil/', include('usuarios.urls'), name="admin_perfil"),
    path('crear-administrador/', views.crear_admin, name="crear_admin"),
    #path('login/', include('usuarios.urls'), name="login"),
    path('admin-libro/', include('libros.urls'), name="admin_libro"),
    path('agregar/', include('libros.urls'), name="agregar_libro"),
    path('listar/', include('libros.urls'), name="listar_libro"),
    path('editar/', include('libros.urls'), name="editar_libro"),
    path('eliminar/', include('libros.urls'), name="eliminar_libro"),
    path('gestionar-admin/', views.gestionar_admin, name="Gestionar_admin"),
    path('eliminar-admin/', views.eliminar_admin, name="Eliminar Administrador"),
    #path('completar-perfil/', include('usuarios.urls'), name="completar_perfil"),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
