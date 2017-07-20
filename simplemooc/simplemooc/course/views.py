from django.shortcuts import render, get_object_or_404,redirect
#importando o model de cursos para trabalhar com base de dados
from .models import Course
#importando formulario de cursos/duvidas
from .forms import ContactCourse
from django.contrib.auth.decorators import login_required
from simplemooc.accounts.models import Enrollment
from django.contrib import messages

def index(request):
    #buscando todos os cursos
    courses = Course.objects.all()
    #definindo tamplete a ser renderizado
    templateName = 'courses/index.html'
    #dicionario de dados para passar para pagina de cursos
    context = {
     'courses': courses
    }
    return render(request, templateName,context)

def details(request, slug):
    #buscando curso deacordo com sua chave primaria, caso não exista tranferir usuario para pagina de erro 404.
    course = get_object_or_404(Course, slug=slug)
    #variavel de dicionario de dados
    context = {}
    #verificando se a uma request
    if request.method == 'POST':
        form = ContactCourse(request.POST)
        if form.is_valid():
            context['is_valid'] = True
            form.sendEmail(course,)
            form = ContactCourse()
    else:
        form = ContactCourse()

    #definindo tamplete a ser renderizado
    templateName = 'courses/details.html'
    #dicionario de dados para passar para pagina de cursos
    context['form'] = form
    context['course'] = course
    return render(request, templateName,context)

@login_required
def enrollment(request,slug):
     #buscando curso deacordo com sua chave primaria, caso não exista tranferir usuario para pagina de erro 404.
     course = get_object_or_404(Course, slug=slug)
     enrollment ,created = Enrollment.objects.get_or_create(user=request.user,course=course)
     if created:
        # enrollment.active()
         messages.success(request, "Parabéns Você acaba de se escrever ao curso !")
     else:
         messages.info(request, "Ops, Você já esta escrito neste curso.")
     return redirect('accounts:dashboard')
