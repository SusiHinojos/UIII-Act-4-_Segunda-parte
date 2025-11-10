from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    # Empleados (ya existentes)
    path('agregar/', views.agregar_empleado, name='agregar_empleado'),
    path('ver/', views.ver_empleados, name='ver_empleado'),
    path('actualizar/<int:id_emp>/', views.actualizar_empleado, name='actualizar_empleado'),
    path('realizar_actualizacion/<int:id_emp>/', views.realizar_actualizacion_empleado, name='realizar_actualizacion_empleado'),
    path('borrar/<int:id_emp>/', views.borrar_empleado, name='borrar_empleado'),

    # Clientes (nuevas rutas)
    path('clientes/agregar/', views.agregar_cliente, name='agregar_cliente'),
    path('clientes/ver/', views.ver_cliente, name='ver_cliente'),
    path('clientes/actualizar/<int:id_cli>/', views.actualizar_cliente, name='actualizar_cliente'),
    path('clientes/realizar_actualizacion/<int:id_cli>/', views.realizar_actualizacion_cliente, name='realizar_actualizacion_cliente'),
    path('clientes/borrar/<int:id_cli>/', views.borrar_cliente, name='borrar_cliente'),
]
