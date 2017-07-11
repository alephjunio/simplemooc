from django.conf.urls import  url, include
from django.contrib.auth import views as auth_views
from simplemooc.accounts import views as accounts_views



#declaração de url amigaveis para app core
urlpatterns = [
    url(r'^entrar/$', auth_views.login,
    {'template_name':'accounts/login.html'} ,name='login'),

    url(r'^sair/$', auth_views.logout,
    {'next_page':'core:home'} ,name='logout'),

    url(r'^cadastrar/$', accounts_views.register , name='register'),
]
