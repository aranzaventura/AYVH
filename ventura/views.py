from django.shortcuts import render

def inicio(request):
    return render (request, "ventura/inicio.html")
def registro(request):
    return render (request, "ventura/formregistro.html")

