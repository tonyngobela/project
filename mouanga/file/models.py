from django.db import models


# Create your models here.
class utilisateur(models.Model):
    nom=models.CharField(max_length=100)
    email=models.EmailField()
    date=models.DateField()
    image=models.ImageField(upload_to='images/')

    
