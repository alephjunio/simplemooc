from django.shortcuts import render,redirect, get_object_or_404
#importando formulario de registro de contas do django
from django.contrib.auth.forms import (UserCreationForm , PasswordChangeForm,SetPasswordForm)
#importando auth e login próprio django
from django.contrib.auth import authenticate, login, get_user_model
#importando app django para ser solicitado login para acessar pagina
from django.contrib.auth.decorators import login_required
#importando settings raiz
from django.conf import settings
from django.contrib import messages
#importando formulario personalizado de CRUD de contas de usuarios
from .forms import RegisterForm ,EditAccountForm, PasswordResetForm
from simplemooc.core.utils import generate_hash_key
from simplemooc.course.models import Enrollment

from .models import PasswordReset

User = get_user_model()


@login_required
def dashboard(request):
    #adicionando valor a variavel com camiho do template
    template_name = 'accounts/dashboard.html'
    context = {}
    context['enrollments'] = Enrollment.objects.filter(user=request.user)
    #retornando template index
    return render(request,template_name,context)



#metodo para cadastrar usuarios
def register(request):
    #adicionando valor a variavel com camiho do template
    template_name = 'accounts/register.html'
    #verificando se o metodo de envio é post
    form = RegisterForm(request.POST or None)
        #vereficando se é valido o formulario
    if form.is_valid():
            #salvar informação no db se dados for valido e captura os dados
            user = form.save()
            #pega usuario para automaticamente autêntica-lo e redirecionar para pagina inicial
            user = authenticate(
                username=user.username, password=form.cleaned_data['password1']
            )
            login(request,user)
            return redirect('core:home')
    context = {
        'form' : RegisterForm()
    }

    return render(request,template_name,context)


def password_reset(request):
    template_name = 'accounts/password_reset.html'
    form = PasswordResetForm(request.POST or None)
    context={}
    if form.is_valid():
        form.save()
        context['success'] = True
    context['form'] = form

    return render(request,template_name,context)

def password_reset_confirm(request,key):
    template_name = 'accounts/password_reset_confirm.html'
    context = {}
    reset = get_object_or_404(PasswordReset,key=key)
    form = SetPasswordForm(user=reset.user, data=request.POST or None)
    if form.is_valid():
        form.save()
        context['success'] = True
    context['form'] = form
    return render(request,template_name,context)

#metodo para editar dados de usuario
@login_required
def edit(request):
    #adicionando valor a variavel com camiho do template
    template_name = 'accounts/edit.html'
    # criando contexto
    context = {}
    form = EditAccountForm(request.POST or None , instance=request.user)
        #vereficando se é valido o formulario
    if form.is_valid():
             #salvar informação no db se dados for valido e captura os dados
             form.save()
             context['success'] = True
             # mensagem de sucesso se tudo ocorrer bem
    context['form'] = form
    #retornado template juntamente com o dicionario
    return render(request,template_name,context)


#Atualizar a senha de usuario
@login_required
def edit_password(request):
    #adicionando valor a variavel com camiho do template
    template_name = 'accounts/edit_password.html'
     # criando contexto
    context = {}
    form = PasswordChangeForm(data=request.POST or None, user=request.user)
    if form.is_valid():
             #salvar informação no db se dados for valido e captura os dados
             form.save()
             # mensagem de sucesso se tudo ocorrer bem
             context['success'] = True
    context['form'] = form

    return render(request,template_name,context)
