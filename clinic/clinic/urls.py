"""
URL configuration for clinic project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from client import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.acceill, name= 'acceill'),
    path("about/",views.about, name= 'about'),
    path("team/",views.team, name='team'),
    path("services/",views.service, name='service'),
    path("ajout/services",views.ajoutservice, name='ajoutservice'),
    path("appointment/",views.appointment, name='appointment'),
    path("gallery/",views.gallery, name='gallery'),
    path("contact",views.contact, name='contact'),
    
    
    path ("Register",views.compte, name="register"),
    path("logins",views.connexion, name="logins"),
    path ("emails",views.email, name="email"),
    
]
