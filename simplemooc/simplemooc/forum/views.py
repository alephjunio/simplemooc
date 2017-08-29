from django.shortcuts import render,redirect
from django.views.generic import TemplateView, View, ListView,DetailView
from django.contrib import messages

from .forms import ReplyForm

from .models import Thread


# class ForumView(View):

#     # template_name = 'forum/index.html'
#     def get(self, request, *args, **kwargs):
#         return render(request, 'forum/index.html')


# class ForumView(TemplateView):

#     template_name = 'forum/index.html'

class ForumView(ListView):

    paginate_by = 4
    template_name = 'forum/index.html'

    def get_queryset(self):
        queryset = Thread.objects.all()
        order = self.request.GET.get('order', '')
        if order == 'views':
            queryset = queryset.order_by('-views')
        elif order == 'answers':
            queryset = queryset.order_by('-answers')
        tag = self.kwargs.get('tag', '')
        if tag:
            queryset = queryset.filter(tags__slug__icontains=tag)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(ForumView, self).get_context_data(**kwargs)
        context['tags'] = Thread.tags.all()
        return context



class ThreadView(DetailView):

    model = Thread
    template_name = 'forum/thread.html'

# Contar a quantidade de vizualizações e adicionar mais um quando post for requisitado.
# adicionar mais uma vizualização somente quanto não for o usuario do post

    def get(self, request, *args, **kwargs):
        response = super(ThreadView, self).get(request, *args, **kwargs)
        if not self.request.user.is_authenticated() or \
           (self.object.author != self.request.user):
           self.object.views = self.object.views + 1
           self.object.save()
        return response

# Criar contexto para view diacordo com os parametros da url
    def get_context_data(self, **kwargs):
        context = super(ThreadView, self).get_context_data(**kwargs)
        context['tags'] = Thread.tags.all()
        context['form'] = ReplyForm(self.request.POST or None)
        return context

#submeter fomlulario de respostas de post
    def post(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated():
            messages.error(
                self.request,
                'Para responder ao tópico é necessário ter efetuado login'
            )
            return redirect(self.request.path)
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        form = context['form']
        if form.is_valid():
            reply = form.save(commit=False)
            reply.thread = self.object
            reply.author = self.request.user
            reply.save()
            messages.success(
                self.request, 'A sua responsta foi enviada com sucesso'
            )
            context['form'] = ReplyForm()
        return self.render_to_response(context)



#Tranformando view paseadas em classes em views paseadas em funções
#chamanda da classe em função
index = ForumView.as_view()
thread = ThreadView.as_view()
