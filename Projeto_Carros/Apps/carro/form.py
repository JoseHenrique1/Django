from .models import Carro
from django import forms

class FormCarro(forms.ModelForm):
    class Meta():

        model = Carro
        fields = '__all__'
