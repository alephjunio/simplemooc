from django.core.urlresolvers import reverse
from django.db import models



class CourseManager(models.Manager):
#metodo de busca nos campos nome ,descrição e slug
    def search(self,query):
            return self.get_queryset().filter(
            models.Q(name__icontains=query) | \
            models.Q(description__icontains=query) | \
            models.Q(slug__icontains=query)
            )

# classe de criação de tabela cursos
class Course(models.Model):

        name = models.CharField('Nome', max_length=100)
        slug = models.SlugField('Atalho')
        description = models.TextField('Descrição', blank=True)
        start_date = models.DateField('Data de Inicio', null=True, blank=True)
        about = models.TextField('Sobre o Curso', blank=True)
        image = models.ImageField(upload_to='course/images', verbose_name='Imagem', null=True, blank=True)

        created_at = models.DateTimeField('Criado em', auto_now_add=True)
        update_at = models.DateTimeField('Atualizado em', auto_now=True)

#chamando metodo da class CourseManager para realizar buscas
        objects = CourseManager()

#convertendo sainda de object e class para nome do object
        def __str__(self):
            return self.name

#contruindo urls amigaveis de acordo com slug
        @models.permalink
        def get_absolute_url(self):
            return ('course:details',(),{'slug': self.slug })

#traduzindo nomes atraves de metas
        class Meta:
            verbose_name = 'Curso'
            verbose_name_plural = 'Cursos'
            ordering = ['name']
