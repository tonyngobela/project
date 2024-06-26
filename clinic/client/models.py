from django.db import models



# Create your models here.
class Service(models.Model):
    nom= models.CharField(max_length=40 , unique=True ,null=True)
    def __str__(self):
        return self.nom
    
class Docteur(models.Model):
    nom=models.CharField(max_length=30)
    prenom=models.CharField(max_length=30)
    sexe=models.CharField(max_length=1)
    age=models.IntegerField
    service=models.ForeignKey("service", on_delete=models.DO_NOTHING)
    def __str__(self):
        return f" {self.nomdoc} {self.prenomdoc} {self.sexe} {self.age}"
    
    
class utilisateur(models.Model):
    nom=models.CharField(max_length=100)
    email=models.EmailField()
    date=models.DateField()
