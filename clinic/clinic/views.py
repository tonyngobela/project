from django.shortcuts import render

def acceuilclinique(request):
    return render(request,'clinique/index.html')