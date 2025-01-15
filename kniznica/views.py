from django.shortcuts import render, HttpResponse
from . models import * #naimportovanie všetkych modelov z models.py v tomto priecčinku

# Create your views here.

def index(request):
    return render(request, "kniznica/index.html")

def list_knihy(request):
    kniha = Kniha.objects.all()
    autor = Autor.objects.all()
    miesto = Miesto.objects.all()
    vydavatel = Vydavatel.objects.all()
    return render(request, "kniznica/index.html", {'knihy': kniha , 'autori': autor, 'miesta': miesto,'vydavatelia': vydavatel,})

def list_autori(request):
    autori = Autor.objects.all()
    return render(request, "kniznica/index.html", {'autori': autori})

def list_vydavatelia(request):
    vydavatelia = Vydavatel.objects.all()
    return render(request, "kniznica/index.html", {'vydavatelia': vydavatelia})  

def list_miesta(request):
    miesta = Miesto.objects.all()
    return render(request, "kniznica/index.html", {'miesta': miesta})