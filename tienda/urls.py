from django.urls import path
from . import views

urlpatterns = [
    path('', views.tiendaProductoIndex),
    path('productoCompra/<idProduct>', views.tiendaProductoCompra),
    path('productoCompra/facturacion/', views.productoComprarSend),
    path('crearProducto/productoCrearSend/', views.productoCrearSend),
    path('crearProducto/', views.tiendaProductoCrear),
]
