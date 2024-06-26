from django.contrib import admin
from django.urls import path
from file import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path ("",views.home, name="urlhome"),
    path ("acceuil",views.acceuil, name="urlacceuil"),
    path ("login",views.connexion, name="urllogin"),
    path ("register",views.compte, name="urlregister"),
    path ("logout",views.deconnexion, name="urldeconnexion"),
    path ("emails",views.email, name="urlemail"),
    path ("reset passwor/<int:pk>",views.reset, name="urlreset"),
     path('affiche',views.afficher,name='urlaffiche'),
     path('ajouter',views.creation,name='urlajouter'),
    path('modifier/<int:pk>',views.modification,name='urlmodifier'),
    path('edites/<int:pk>/',views.edite,name='urledite'),
    path('supprimer/<int:pk>/',views.supprimer,name='urlsupprimer'),
]
