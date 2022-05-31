from django.urls import path
from . import views

urlpatterns = [
    path('', views.tipoDocumentoIndex),
    path('crear/', views.tipoDocumentoCrear)
]
