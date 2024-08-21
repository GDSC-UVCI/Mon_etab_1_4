from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('eleve/', views.eleve, name='eleve'),
    path('eleve/ajouter', views.ajouter_eleve, name='ajouter_eleve'),
    path('eleve/modifier', views.modifier_eleve, name='modifier_eleve'),
    path('professeur/', views.professeur, name='professeur'),
    path('professeur/ajouter', views.ajouter_professeur, name='ajouter_professeur'),
    path('professeur/modifier', views.modifier_professeur, name='modifier_professeur'),
    path('utilisateur/', views.utilisateur, name='utilisateur'),
    path('utilisateur/ajouter', views.ajouter_utilisateur, name='ajouter_utilisateur'),
    path('utilisateur/modifier', views.modifier_utilisateur, name='modifier_utilisateur'),
    path('rapport/', views.rapport, name='rapport'),
    path('login/', views.login, name='login'),
]