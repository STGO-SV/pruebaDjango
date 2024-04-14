from django.shortcuts import render

# Create your views here.
def home(request):
    lista = ["Borgoña","Batman","Completo"]
    contexto = {"mascotas": lista}
    return render(request,'core/home.html',contexto)

def borgona(request):
    contexto = {"nombreMascota": "*Borgoña*","Edad":"3 años"}
    return render(request,'core/borgona.html',contexto)

def batman(request):
    contexto = {"nombreMascota": "Batman","Edad": "2 años"}
    return render(request,'core/batman.html',contexto)
