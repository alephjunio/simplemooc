from django.conf.urls import url
#importanto o app core com views
from simplemooc.core import views

#declaração de url amigaveis para app core
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^contato/$', views.contact, name='contact'),

]
