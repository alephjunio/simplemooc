from django.conf.urls import url

#importanto o app forum com views
from simplemooc.forum import views


#declaração de url amigaveis para app forum
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^tag/(?P<tag>[\w_-]+)/$', views.index, name='index_tagged'),
    url(r'^respostas/(?P<pk>\d+)/correta$', views.reply_correct, name='reply_correct'),
    url(r'^respostas/(?P<pk>\d+)/incorreta$', views.reply_incorrect, name='reply_incorrect'),
    url(r'^(?P<slug>[\w_-]+)/$', views.thread, name='thread'),
]
