from django.urls import path
from . import views

urlpatterns = [
    path('', views.tipoLicores),
    path('registrar/', views.registrarTiposLicores),
    path('editar/<idTypeDrink>', views.editarTiposLicores), 
    path('editar/editarTipoLicor/', views.modificarTiposLicores),
    path('eliminar/<idTypeDrink>', views.eliminarTiposLicores),
]
