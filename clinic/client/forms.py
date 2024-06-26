from django import forms
from .models import docteur,service




class doctuerform(forms.ModelForm):
    class Meta:
        model=docteur
        fields=['nomdoc','prenomdoc','sexe','age']