from django import forms
from django.forms import ModelForm
from serialmail.models import MailProvider


class UploadFileForm(forms.Form):
    file = forms.FileField()


class EmailProviderForm(ModelForm):
    class Meta:
        model = MailProvider
        fields = ['user', 'password', 'server']
        widgets = {
            'password': forms.PasswordInput(attrs={'placeholder': 'Hasło'}),
            'user': forms.TextInput(attrs={'placeholder': "Użytkownik"}),
            'server': forms.TextInput(attrs={'placeholder': "Serwer"})
        }
        labels = {
            'password': "",
            'user': "",
            'server': ""
        }
