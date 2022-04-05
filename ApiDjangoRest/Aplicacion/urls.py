from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.ListarProductos, name='index'),
    path('index/categorias', views.ListarCategorias, name='categorias'),
    path('index/agregarcategoria', views.AgregarCategorias, name='agregarcategoria'),
    path('index/agregar', views.AgregarProductos, name='agregar'),
    path('index/filtrar/<str:categoria>', views.FiltrarProductos, name="filtrar"),
    path('index/borrar/<str:pk>/', views.BorrarProducto, name='borrar'),
    path('index/borrarcategoria/<str:pk>/', views.BorrarCategoria, name = "borrarcategoria")
]