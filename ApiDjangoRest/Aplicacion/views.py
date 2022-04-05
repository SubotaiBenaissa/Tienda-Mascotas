
from .models import Categoria, Producto
from django.shortcuts import redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductoSerializer, CategoriaSerializer

# Create your views here.

@api_view(['GET'])
def ListarProductos(request):

    producto = Producto.objects.all()
    serializer = ProductoSerializer(producto, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def ListarCategorias(request):

    categoria = Categoria.objects.all()
    serializer = CategoriaSerializer(categoria, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def FiltrarProductos(request, categoria):

    producto = Producto.objects.filter(categoria = categoria)
    serializer = ProductoSerializer(producto, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def AgregarProductos(request):

    serializer = ProductoSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def AgregarCategorias(request):

    serializer = CategoriaSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def BorrarProducto(request, pk):
    
    producto = Producto.objects.get(id = pk)
    producto.delete()
    return redirect('index')

@api_view(['DELETE'])
def BorrarCategoria(request, pk):

    categoria = Categoria.objects.get(id = pk)
    categoria.delete()
    return redirect('index')