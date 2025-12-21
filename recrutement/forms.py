from django import forms
from .models import Postule


class PostuleForm(forms.ModelForm):
    class Meta:
        model = Postule
        fields = [
            'diplome',
            'nom',
            'prenom',
            'lieu_n',
            'zone',
            'image',
            'carte_i',
            'diplome_pdf',
        ]
        widgets = {
            'diplome': forms.Select(attrs={'class': 'form-select'}),
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'prenom': forms.TextInput(attrs={'class': 'form-control'}),
            'lieu_n': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'zone': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'carte_i': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'diplome_pdf': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }