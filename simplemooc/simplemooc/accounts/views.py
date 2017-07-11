from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings

from .forms import RegisterForm

def register(request):
    #adicionando valor a variavel com camiho do template
    template_name = 'accounts/register.html'
    #verificando se o metodo de envio é post
    if request.method == 'POST':
        #atribuir dados em variavel form
        form = RegisterForm(request.POST)
        print(form)
        #vereficando se é valido o formulario
        if form.is_valid():
            #salvar informação no db se dados for valido
            form.save()
            return redirect(settings.LOGIN_URL)
    context = {
        'form' : RegisterForm()
    }

    return render(request,template_name,context)
