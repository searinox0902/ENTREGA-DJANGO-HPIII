import uuid
from django.db import models
from tiposLicores.models import TiposLicores
from tiposDocumento.models import TiposDocumento

# Create your models here.

class Producto(models.Model):
    idProduct       = models.CharField(max_length=6, primary_key=True)
    title           = models.CharField(max_length=100)
    description     = models.TextField(max_length=300)
    mark            = models.CharField(max_length=30)
    value           = models.CharField(max_length=30)
    dateCreation    =  models.DateField('Fecha de Creacón', auto_now=True)
    image           =  models.CharField(max_length=100)
    stock           =  models.CharField(max_length=5)

    # RELACIONES 
    TipoLicor       = models.ForeignKey(TiposLicores, null=True, blank=True, on_delete=models.CASCADE )


class RegistroCompra(models.Model):
    idBuy   = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    idUser  = models.CharField(max_length=30)
    fullName = models.CharField(max_length = 40)  
    email = models.CharField(max_length = 40)
    departament = models.CharField(max_length = 20)
    city = models.CharField(max_length = 20)
    address = models.CharField(max_length = 40)
    phone = models.CharField(max_length = 40)
    value = models.CharField(max_length = 12)
    #ForeingKey 
    idProduct = models.ForeignKey(Producto, null=True, blank=True, on_delete=models.CASCADE )
    typeDocument = models.ForeignKey(TiposDocumento, null=True, blank=True, on_delete=models.CASCADE )

