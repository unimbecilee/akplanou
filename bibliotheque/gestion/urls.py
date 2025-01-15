from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_view, name='dashboard'),
    path('membres/', views.gestion_membres_view, name='gestion_membres'),
    path('livres/', views.gestion_livres_view, name='gestion_livres'),
    path('abonnements/', views.gestion_abonnements_view, name='gestion_abonnements'),
    path('emprunts/', views.gestion_emprunts_view, name='gestion_emprunts'),
    path('exemplaires/', views.gestion_exemplaires_view, name='gestion_exemplaires'),
    path('membre/<int:membre_id>/', views.membre_detail_view, name='membre_detail'),
    path('livre/<int:livre_id>/', views.livre_detail_view, name='livre_detail'),
    path('ajouter_membre/', views.ajouter_membre_view, name='ajouter_membre'),
    path('ajouter_livre/', views.ajouter_livre_view, name='ajouter_livre'),
    path('ajouter_abonnement/', views.ajouter_abonnement_view, name='ajouter_abonnement'),
    path('ajouter_exemplaire/', views.ajouter_exemplaire_view, name='ajouter_exemplaire'),
    path('ajouter_emprunt/', views.ajouter_emprunt_view, name='ajouter_emprunt'),
    path('retour/<int:emprunt_id>/', views.retour_view, name='retour'),
    path('historique/<int:membre_id>/', views.historique_view, name='historique'),
    path('load_exemplaires/<int:livre_id>/', views.load_exemplaires, name='load_exemplaires'),
    path('modifier_livre/<int:livre_id>/', views.modifier_livre_view, name='modifier_livre'),
    path('supprimer_livre/<int:livre_id>/', views.supprimer_livre_view, name='supprimer_livre'),
    path('modifier_abonnement/<int:abonnement_id>/', views.modifier_abonnement_view, name='modifier_abonnement'),
    path('modifier_membre/<int:membre_id>/', views.modifier_membre_view, name='modifier_membre'),
    path('supprimer_membre/<int:membre_id>/', views.supprimer_membre_view, name='supprimer_membre'),
    path('supprimer_abonnement/<int:abonnement_id>/', views.supprimer_abonnement_view, name='supprimer_abonnement'),
]