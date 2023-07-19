from .models import Cliente
from django import forms

class FormCliente(forms.ModelForm):
    class Meta():
        model = Cliente
        fields = '__all__'