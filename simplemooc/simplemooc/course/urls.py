from django.conf.urls import url

#importanto o app courses com views
from simplemooc.course import views


#declaração de url amigaveis para app courses
urlpatterns = [
    url(r'^$', views.index, name='index'),
    #passando parametro via url para consulta de base de dados
    url(r'^(?P<slug>[\w_-]+)/$', views.details, name='details'),
    #url(r'^(?P<pk>\d+)/$', views.details, name='details'),
]
