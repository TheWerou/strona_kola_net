from django import forms
from .models import Comunication


class EmailForm(forms.ModelForm):
    temat = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'id': 'contact-subject', 'arialabel': 'Temat', 'placeholder': 'Temat'
               }))

    tekst = forms.CharField(required=True, widget=forms.Textarea(
        attrs={'class': 'form-control', 'id': 'contact-message','arialabel': 'Wiadomość', 'placeholder': 'Wiadomość'
                                                                         }))

    class Meta:
        model = Comunication
        fields = ['temat', 'tekst',]

