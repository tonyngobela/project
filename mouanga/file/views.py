from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from file.models import utilisateur

# Create your views here.
#protection de la page
@login_required(login_url='urllogin')
def home (request):
    
    return render(request,"index.html")

def acceuil(request):
    
    return render(request,"acceuil.html")


def connexion(request):
    if request.method == 'POST':
        data = request.POST
        username = data.get('username')
        password = data.get('password')
        user = authenticate(username = username , password = password)
        if user:
            login(request,user)
            print("connexion reussie")
            return redirect('urlhome')
        else:
            print("desolé mot de passe incorrect")
            return redirect('urllogin')


    return render(request,"login.html")


def deconnexion(request):
    logout(request)
    print('deconnexion reussie')
    return redirect('urllogin')

    


def compte(request):
    if request.method =='POST':
        data =request.POST
        if data.get('password') == data.get('password1'):
            username = data.get ('username')
            email =data.get ('email')
            password =data.get ('password')
            print(f"{username},\n {email},\n {password}")
            toto =User.objects.create_user(
                username = username,
                email = email,
                password = password
            )
            print("le compte créé avec succes !!")
            return redirect('urllogin')

        else:
            print("le compte n'a pas été créé")

    
    
    return render(request,"register.html")

def email(request):
    if request.method=="POST":
        data=request.POST
        email=data.get('email')
        user=User.objects.filter(email=email).last()
        if user:
            print("Email correct ")
            return redirect('urlreset',user.id)
        else:
            print("email incorrect")
            return redirect("urlemail")
        
    
    return render(request,"email.html")

def reset (request,pk):
    user=User.objects.get(pk=pk)
    if request.method=='POST':
        data=request.POST
        if data.get('password')==data.get('password1'):
            newpassword=data.get('newpassword')
            user.set_password(newpassword)
            user.save()
            print('mot de passe modifier avec succes')
            return redirect('urllogin')
        else:
            print("desolée les deux mots de passes ne sont pas identiques ")
            return redirect('urlreset')
        
    return render(request,'reset passwor.html')    


def afficher(request):
    data=utilisateur.objects.all()
    toto={'tata':data}
    return render(request,'affiche.html',toto)


def creation(request):
    if request.method=="POST":
        data=request.POST
        images=request.FILES.get('image')
        toto=utilisateur(
            nom=data.get('nom'),
            email=data.get('email'),
            date=data.get('date'),
            image=images
        )
        toto.save()
        print('ok')
        return redirect('urlaffiche')
    else:
        print('desolee')

        

   
    return render(request,'ajout.html')




def modification(request,pk):
    data=utilisateur.objects.get(pk=pk)
    images=request.FILES.get('image')
    if request.method=="POST":
        toto=request.POST
        data.nom= toto.get('nom')
        data.email= toto.get('email')
        data.date= toto.get('date')
        data.image= images
        data.save()
        return redirect('urlaffiche')
       
    return render(request,'modifir.html')


def edite(request, pk):
    data=utilisateur.objects.get(pk=pk)
    
    return render(request,'edite.html',{'data':data})

def supprimer(request,pk):
    data=utilisateur.objects.get(pk=pk)
    data.delete()
    return redirect('urlaffiche')


    


  