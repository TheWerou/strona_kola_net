from django import forms
from .models import Comunication


class EmailForm(forms.ModelForm):
    imie = forms.CharField(max_length=200, widget=forms.TextInput(
        attrs={'class': 'form-control', 'id': 'contact-name','arialabel': 'Imię', 'placeholder': 'Imię'
                                                                         }))
    nazwisko = forms.CharField(max_length=200, widget=forms.TextInput(
        attrs={'class': 'form-control', 'id': 'contact-surname"','arialabel': 'Nazwisko', 'placeholder': 'Nazwisko'
                                                                         }))
    email = forms.EmailField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'id': 'contact-email','arialabel': 'Email', 'placeholder': 'Email'
                                                                         }))
    temat = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'id': 'contact-subject', 'arialabel': 'Temat', 'placeholder': 'Temat'
               }))

    tekst = forms.CharField(required=True, widget=forms.Textarea(
        attrs={'class': 'form-control', 'id': 'contact-message','arialabel': 'Wiadomość', 'placeholder': 'Wiadomość'
                                                                         }))

    class Meta:
        model = Comunication
        fields = ['imie', 'nazwisko', 'email', 'temat', 'tekst', ]

