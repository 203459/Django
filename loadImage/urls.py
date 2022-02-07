from django.urls import path, re_path
from django.conf.urls import include
from loadImage.views import ImageLoad
from loadImage.views import ImageLoadDetail


urlpatterns = [
    re_path( r'^listaimage/$', ImageLoad.as_view()),
     re_path( r'^listaimage/(?P<pk>\d+)$', ImageLoadDetail.as_view()),
]