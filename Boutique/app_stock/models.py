from django.db import models
import uuid

# Create your models here.
class Produit(models.Model):
    designation=models.CharField(max_length=100)
    prix=models.IntegerField()
    date=models.DateField()
    image=models.ImageField(upload_to='image/')
    secretkey=models.UUIDField(default=uuid.uuid4)
    def __str__(self):
        return self.designation


class Vente(models.Model):
    designation=models.ForeignKey(Produit, on_delete=models.CASCADE, related_name='qteachat')
    pu=models.IntegerField(editable=False)
    qtev=models.IntegerField()
    pttc=models.IntegerField(default=0, editable=False)
    datev=models.DateField()
    secretkey=models.UUIDField(default=uuid.uuid4)

    def __str__(self):
        return f"designation: {self.designation} Quantite: {self.qtev}/, prix: {self.pu}/ pttc:{self.pttc}"

    def save(self,*args,**kwargs):
        self.pu=self.designation.prix
        self.pttc=int(self.pu*self.qtev)
        super().save(*args,**kwargs)


class Stock(models.Model):
    qtes=models.IntegerField()
    Produit=models.OneToOneField(Produit, on_delete=models.CASCADE, related_name='produits')
    secretkey=models.UUIDField(default=uuid.uuid4)
   
   
