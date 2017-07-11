from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.conf import settings

from .forms import RegisterForm

def register(request):
    #adicionando valor a variavel com camiho do template
    template_name = 'accounts/register.html'
    #verificando se o metodo de envio é post
    if request.method == 'POST':
        #atribuir dados em variavel form
        form = RegisterForm(request.POST)
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
