from django.conf.urls import url

#importanto o app forum com views
from simplemooc.forum import views


#declaração de url amigaveis para app forum
urlpatterns = [
    url(r'^$', views.index, name='index'),
]
