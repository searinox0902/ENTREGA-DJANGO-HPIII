from django.shortcuts import render, redirect
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from .models import Producto
from .models import RegistroCompra
from tiposLicores.models import TiposLicores
from tiposDocumento.models import  TiposDocumento
# Create your views here.

def tiendaProductoIndex(request):
    producto = Producto.objects.all()   # traemos todos los registros
    return render(request, "tiendaProductosIndex.html", {"productos" : producto})

def tiendaProductoCrear(request):
    tiposLicoresList = TiposLicores.objects.all()
    return render(request, "productoCrear.html", {"tiposLicoresList" : tiposLicoresList})

def tiendaProductoCompra(request, idProduct):
    tiposDocumentoList =  TiposDocumento.objects.all()
    productoCompra = idProduct
    productoFinal = Producto.objects.get(idProduct=productoCompra)
    return render(request, "productoCompra.html", {"tiposLicoresList" : tiposDocumentoList, "productoFinal" : productoFinal})

def productoCrearSend(request):

    #FK
    typeLicorReference          =   request.POST['tipoLicorTxt']
    tipoLicorResponse           =   TiposLicores.objects.get(idTypeDrink = typeLicorReference)
    typeLicorSend               =   tipoLicorResponse
    idProductSend           =   request.POST['idProduct']   
    titleSend               =   request.POST['titleTxt']
    descriptionSend         =   request.POST['descTxt']
    markSend                =   request.POST['markTxt']
    valueSend               =   request.POST['valueTxt']
    imageSend               =   request.POST['imageTxt']
    stockSend               =   request.POST['stockTxt'] 
    
  
    
    registarProducto = Producto.objects.create(
        idProduct         =      idProductSend,
        title             =      titleSend, 
        description       =      descriptionSend,
        mark              =      markSend,
        value             =      valueSend, 
        image             =      imageSend,
        stock             =      stockSend,
        TipoLicor         = typeLicorSend
    )

    return redirect('/tienda/')

def productoComprarSend(request):

   
    idUserSend          = request.POST['idUserTxt']
    fullNameSend        = request.POST['fullNameTxt']
    emailSend           = request.POST['mailTxt']
    departamentSend     = request.POST['departamentTxt']
    citySend            = request.POST['cityTxt']
    addressSend         = request.POST['addressTxt']
    phoneSend           = request.POST['telTxt']
    valueSend           = request.POST['valueTxt']

    #ForeingKey 
    
    typeDocumentReference          =   request.POST['typeDocumentTxt']
    typeDocumentResponse           =   TiposDocumento.objects.get(idTypeDoc = typeDocumentReference)
    typeDocumentSend               =   typeDocumentResponse
    
    idProductReference              =   request.POST['idProductTxt']
    idProductResponse               =   Producto.objects.get(idProduct=idProductReference)
    idProductSend                   =   idProductResponse

    registarCompra = RegistroCompra.objects.create(
        idUser = idUserSend,           
        fullName = fullNameSend,     
        email = emailSend,   
        departament = departamentSend,    
        city  = citySend,
        address = addressSend, 
        phone = phoneSend,       
        value = valueSend,
        idProduct =  idProductSend,
        typeDocument =    typeDocumentSend
    )

    #EDITAR

    productoDescontarStock = Producto.objects.get(idProduct =  idProductReference)
    
    productoDescontarStock.stock  = int(productoDescontarStock.stock) - 1

    productoDescontarStock.save() 

    #ENVIAR CORREO



    email = EmailMultiAlternatives(
        'Felicidades Has comprado en nuestra app',
        'Aplicacion de Venta de Licores, Gracias por compra en nuestra app',
        settings.EMAIL_HOST_USER,
        [emailSend]
    )
    
    email.send()


    


    return redirect('/tienda/')