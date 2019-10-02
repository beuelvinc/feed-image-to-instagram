from django import forms
from .models import Instagram


class formmodel(forms.ModelForm):
    password=forms.CharField(max_length=120,widget=forms.PasswordInput(attrs={"class":'form-control'}))
    username=forms.CharField(max_length=120,widget=forms.TextInput(attrs={"class":'form-control'}))
    class Meta:
        model=Instagram
        fields='__all__'
        