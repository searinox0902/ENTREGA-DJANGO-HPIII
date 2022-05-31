from django.shortcuts import render

# Create your views here.
def menuPrincipalIndex(request):

    return render(request, "menuPrincipal.html")
