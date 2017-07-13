from django.shortcuts import render,redirect
#importando formulario de registro de contas do django
from django.contrib.auth.forms import UserCreationForm , PasswordChangeForm
#importando auth e login próprio django
from django.contrib.auth import authenticate, login
#importando app django para ser solicitado login para acessar pagina
from django.contrib.auth.decorators import login_required
#importando settings raiz
from django.conf import settings
#importando formulario personalizado de CRUD de contas de usuarios
from .forms import RegisterForm ,EditAccountForm


@login_required
def dashboard(request):
    #adicionando valor a variavel com camiho do template
    template_name = 'accounts/dashboard.html'
    #retornando template index
    return render(request,template_name)



#metodo para cadastrar usuarios
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


#metodo para editar dados de usuario
@login_required
def edit(request):
    #adicionando valor a variavel com camiho do template
    template_name = 'accounts/edit.html'
    # criando contexto
    context = {}
    #verificando se o metodo de envio é post
    if request.method == 'POST':
        #atribuir dados em variavel form
        form = EditAccountForm(request.POST, instance=request.user)
        #vereficando se é valido o formulario
        if form.is_valid():
             #salvar informação no db se dados for valido e captura os dados
             form.save()
             # setando em instancia atual
             form = EditAccountForm(instance=request.user)
             # mensagem de sucesso se tudo ocorrer bem
             context['success'] = True
    else:
        form = EditAccountForm(instance=request.user)
            #alimenttando context que ira ser passado para template edit.html
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
     #verificando se o metodo de envio é post
    if request.method == 'POST':
         form = PasswordChangeForm(data=request.POST, user=request.user)
         if form.is_valid():
             #salvar informação no db se dados for valido e captura os dados
             form.save()
             # mensagem de sucesso se tudo ocorrer bem
             context['success'] = True
    else:
        form = PasswordChangeForm(user=request.user)
    context['form'] = form

    return render(request,template_name,context)
