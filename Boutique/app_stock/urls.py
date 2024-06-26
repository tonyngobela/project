from django.urls import path
from app_stock import views

urlpatterns = [
    path('aa/', views.index, name='urlindex'),
    path('ajoutven/', views.ajoutvente, name='urlajouvent'),
    path('insert/', views.insertion, name='urlinsert'),
    path('affiche/', views.afficheproduit, name='urlaffiche'),
]