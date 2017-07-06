from django.contrib import admin

from .models import Course

class CourseAdmin(admin.ModelAdmin):
    #selecionando conteudo para que possa ser passado para o painel de admin
    list_display = ['name','slug','start_date','created_at']
    #filtro determinando por qual compo ira buscar
    search_fields = ['name','slug']
    #populando automaticamente o campo de atalho com a mesma informação do campo nome trocando espaços por infes ' - ' .
    prepopulated_fields = {'slug': ('name', )}


#adicionando modificações em sua tela de admin
admin.site.register(Course, CourseAdmin)
