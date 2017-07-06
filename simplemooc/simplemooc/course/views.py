from django.shortcuts import render, get_object_or_404
#importando o model de cursos para trabalhar com base de dados
from .models import Course



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


#def details(request, pk):
    ##buscando curso deacordo com sua chave primaria, caso não exista tranferir usuario para pagina de erro 404.
    #course = get_object_or_404(Course, pk=pk)
    ##definindo tamplete a ser renderizado
    #templateName = 'courses/details.html'
    ##dicionario de dados para passar para pagina de cursos
    #context = {
        #'course': course
    #}
    #return render(request, templateName,context)

def details(request, slug):
    #buscando curso deacordo com sua chave primaria, caso não exista tranferir usuario para pagina de erro 404.
    course = get_object_or_404(Course, slug=slug)
    #definindo tamplete a ser renderizado
    templateName = 'courses/details.html'
    #dicionario de dados para passar para pagina de cursos
    context = {
        'course': course
    }
    return render(request, templateName,context)
