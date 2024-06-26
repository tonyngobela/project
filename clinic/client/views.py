from django.shortcuts import render,redirect
from django.template import loader
from client.models import Service,Docteur,utilisateur

from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import AbstractUser
# Create your views here.


def acceill(request):
    return render(request,'client/index.html')

def about(request):
    return render(request,'client/about.html')


def service(request):
    return render(request,'client/service.html')



def ajoutservice(request):
#    nom=request.POST.get('nom')
 #   newservice=Service.objects.create(nom=nom)
  #  newservice.save()
    return render(request,'clinique/formulaireservice.html')

def team(request):
    return render(request,'client/team.html')


def gallery(request):
    return render(request,'client/gallery.html')

def appointment(request):
    return render(request,'client/appointment.html')


def contact(request):
    return render(request,'client/contact.html')

#authentification

@login_required(login_url='urllogin')
def home (request):
    
    return render(request,"index.html")

def acceuil(request):
    
    return render(request,"acceuil.html")


def compte(request):
    if request.method =='POST':
        data =request.POST
        if data.get('password') == data.get('password1'):
            username = data.get ('username')
            email =data.get ('email')
            password =data.get ('password')
            print(f"{username},\n {email},\n {password}")
            toto =User.objects.create_user(
                nom = username,
                email = email,
                password = password
            )
            print("le compte créé avec succes !!")
            return redirect('login')

        else:
            print("le compte n'a pas été créé")

    
    
    return render(request,"clinique/register.html")


def connexion(request):
    if request.method == 'POST':
        data = request.POST
        username = data.get('username')
        password = data.get('password')
        user = authenticate(username = username , password = password)
        if user:
            login(request,user)
            print("connexion reussie")
            return redirect('acceill')
        else:
            print("desolé mot de passe incorrect")
            return redirect('logins')


    return render(request,"client/index.html")


def email(request):
    if request.method=="POST":
        data=request.POST
        email=data.get('email')
        user=User.objects.filter(email=email).last()
        if user:
            print("Email correct ")
            return redirect('reset',user.id)
        else:
            print("email incorrect")
            return redirect("email")
        
    
    return render(request,"clinique/email.html")
