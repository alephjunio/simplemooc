from django.shortcuts import render, get_object_or_404,redirect
#importando o model de cursos para trabalhar com base de dados
from .models import Course ,Enrollment, Announcement
#importando formulario de cursos/duvidas
from .forms import ContactCourse, CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .decorators import enrollment_required

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
     enrollment, created = Enrollment.objects.get_or_create(user=request.user,course=course)
     if created:
        # enrollment.active()
         messages.success(request, "Parabéns Você acaba de se escrever ao curso !")
     else:
         messages.info(request, "Ops, Você já esta escrito neste curso.")
     return redirect('accounts:dashboard')

@login_required
def undo_enrollment(request,slug):
    #buscando curso deacordo com sua chave primaria, caso não exista tranferir usuario para pagina de erro 404.
    course = get_object_or_404(Course, slug=slug)
    enrollment = get_object_or_404(Enrollment,user=request.user,course=course)
    if request.method == 'POST':
        enrollment.delete()
        messages.success(request,'Sua inscrição foi cancelada com sucesso')
    template_name = 'courses/undo_enrollment.html'
    context = {
     'enrollment': enrollment,
     'course': course
    }
    return render(request,template_name,context)


@login_required
@enrollment_required
def announcements(request,slug):
    #buscando curso deacordo com sua chave primaria, caso não exista tranferir usuario para pagina de erro 404.
    course = request.course
    context = {}
    context['course'] = course
    context['announcements'] = course.announcements.all()
    template_name = 'courses/announcements.html'
    return render(request,template_name,context)

@login_required
@enrollment_required
def show_announcement(request,slug,pk):
    #buscando curso deacordo com sua chave primaria, caso não exista tranferir usuario para pagina de erro 404.
    course = course = request.course
    announcement = get_object_or_404(course.announcements.all(), pk=pk)
    form = CommentForm(request.POST  or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.user = request.user
        comment.announcement = announcement
        comment.save()
        form = CommentForm()
        messages.success(request, 'Seu comentário foi salvo com sucesso!')

    template_name = 'courses/show_announcement.html'
    context = {}
    context['course'] = course
    context['announcement'] = announcement
    context['form'] = form

    return render(request,template_name, context)
