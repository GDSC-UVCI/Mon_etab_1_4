from django.shortcuts import render


# Create your views here.
def dashboard(request):
    return render(request, 'eleve/index.html')

def eleve(request):
    return render(request, 'eleve/three.html')

def ajouter_eleve(request):
    return render(request, 'eleve/four.html')

def modifier_eleve(request):
    return render(request, 'eleve/five.html')

def professeur(request):
    return render(request, 'eleve/seven.html')

def modifier_professeur(request):
    return render(request, 'eleve/nine.html')

def ajouter_professeur(request):
    return render(request, 'eleve/eight.html')

def utilisateur(request):
    return render(request, 'eleve/eleven.html')

def ajouter_utilisateur(request):
    return render(request, 'eleve/twelve.html')

def modifier_utilisateur(request):
    return render(request, 'eleve/fourteen.html')

def rapport(request):
    return render(request, 'eleve/thirteen.html')

def login(request):
    return render(request, 'eleve/login.html')


