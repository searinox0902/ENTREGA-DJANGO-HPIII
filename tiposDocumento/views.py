from django.shortcuts import render, redirect
from .models import TiposDocumento
# Create your views here.


def tipoDocumentoIndex(request):
    TipoDocumento = TiposDocumento.objects.all()
    return render(request, "tipoDocumentoIndex.html", {"tipoDocumento" : TipoDocumento})

def tipoDocumentoCrear(request):
    descriptionTxt = request.POST['descriptionTxt']
    
    nuevoTipoDocumento = TiposDocumento.objects.create(
        description = descriptionTxt
    )

    return redirect('/tiposDocumento/')