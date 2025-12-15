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