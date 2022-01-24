from django.urls import path, re_path
from django.conf.urls import include

from Register.views import UserAdd

urlpatterns = [
    re_path( r'^add/$', UserAdd.as_view()),
]