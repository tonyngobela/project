from django.shortcuts import render
from app_stock.models import Produit, Vente, Stock

# Create your views here.
def index(request):
    return render(request, 'index.html')


def ajoutvente(request):
    data=Produit.objects.all()
    return render(request,'formulaireven.html',{'data':data})


def insertion(request):
    if request.method=="POST":
        data=request.POST
        photo=request.FILES.get('image')
        insertion=Produit(
            designation=data.get('designation'),
            prix=data.get('prix'),
            date=data.get('date'),
            image=photo
        )
        if isinstance is not None:
            insertion.save()
        else:
            print("les données ne sont pas completes")

        print("ok")
    else:
        print("non")
    return render(request,'insertion.html')


def afficheproduit(request):
    data=Produit.objects.all()
    toto={'data':data}
    return render(request, 'afficheproduit.html', toto)
    
