from django.shortcuts import render
from car.models import Fotografia

# Create your views here.
def index(request):
    
    fotografias=Fotografia.objects.all()
    return render(request, 'galeria/index.html',{"cards":fotografias})


def imagem(request):
    return render(request, 'galeria/imagem.html')




