from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


#realizar registro de usuarios
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


#realizar editar de usuarios
class EditAccountForm(forms.ModelForm):

    #consultar email para validar se já é existente em base de dados
    def clean_email(self):
        #capturar email
        email = self.cleaned_data['email']
        query_set = User.objects.filter(email=email).exclude(pk=self.instance.pk)
        if query_set.exists():
            raise forms.ValidationError('Já existe usuáior com este E-mail')
        return email

    #informando quais campos podera ser editados pelo usuario
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name']
