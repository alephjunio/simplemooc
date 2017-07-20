from django.conf.urls import  url, include
from django.contrib.auth import views as auth_views
from simplemooc.accounts import views as accounts_views



#declaração de url amigaveis para app core
urlpatterns = [
    url(r'^$', accounts_views.dashboard , name='dashboard'),
    url(r'^entrar/$', auth_views.login,{'template_name':'accounts/login.html'} ,name='login'),
    url(r'^sair/$', auth_views.logout,{'next_page':'core:home'} ,name='logout'),
    url(r'^cadastrar/$', accounts_views.register , name='register'),
    url(r'^editar/$', accounts_views.edit , name='edit'),
    url(r'^editar-senha/$', accounts_views.edit_password , name='edit_password'),
    url(r'^nova-senha/$', accounts_views.password_reset , name='password_reset'),
    url(r'^confirmar-nova-senha/(?P<key>\w+)/$', accounts_views.password_reset_confirm , name='password_reset_confirm')
]
