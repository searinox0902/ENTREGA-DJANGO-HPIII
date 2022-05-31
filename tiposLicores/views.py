from django.shortcuts import render, redirect
from .models import TiposLicores
# Create your views here.

def tipoLicores(request):
    tlicores = TiposLicores.objects.all()
    return render(request, "gestionTipoLicor.html", {"TipoLicores" : tlicores})

def registrarTiposLicores(request):
    idForm = request.POST['idTxt']
    nameForm = request.POST['nameTxt']
    
    nuevoTipoLicor = TiposLicores.objects.create(
        idTypeDrink = idForm,
        name = nameForm
    )

    return redirect('/tiposLicores/')


def eliminarTiposLicores(reqest, idTypeDrink):
    tipoLicor = TiposLicores.objects.get(idTypeDrink=idTypeDrink)
    tipoLicor.delete()

    return redirect('/tiposLicores/')

#Envia a la pantalla editar el items seleccionado

def editarTiposLicores(request, idTypeDrink):
    tipoLicor = TiposLicores.objects.get(idTypeDrink=idTypeDrink)
    return render(request, "editarTipoLicor.html", {"TipoLicores" : tipoLicor})

#Accion de la pantalla destino de editar

def modificarTiposLicores(request):
    idForm = request.POST['idTxt']
    nameForm = request.POST['nameTxt']

    tipoLicor = TiposLicores.objects.get(idTypeDrink=idForm)
    tipoLicor.name = idForm
    tipoLicor.name = nameForm

    tipoLicor.save() 

    return redirect('/tiposLicores/')