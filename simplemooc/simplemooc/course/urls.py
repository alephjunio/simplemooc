from django.conf.urls import url
#importanto o app courses com views
from simplemooc.course import views

#declaração de url amigaveis para app courses
urlpatterns = [
    url(r'^', views.index, name='index'),
]
