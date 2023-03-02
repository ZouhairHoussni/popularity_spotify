from django import forms
from .models import MyModel

class MyForm(forms.ModelForm):
    chanson = forms.CharField(label='Entrez le nom de la chanson :', error_messages={'required': ''})
    class Meta:
        model = MyModel
        fields = ['chanson']