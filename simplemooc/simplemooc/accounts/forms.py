from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class RegisterForm(UserCreationForm):

        email = forms.EmailField(label='E-mail')

        # Verificar se email ja é existente em base de dados
        def clean_email(self):
            #capturar email
            email = self.cleaned_data['email']
            #consultar email.
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError('Já existe usuáior com este E-mail')
            return email

#travar transissão de save e capturar dados de email e apos isso continuar o commit em base de dados
        def save(self,commit=True):
                user = super(RegisterForm,self).save(commit=False)
                user.email = self.cleaned_data['email']
                if commit:
                   user.save()
                return user
