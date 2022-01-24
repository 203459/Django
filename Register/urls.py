from django.urls import path, re_path
from django.conf.urls import include

from Register.views import RegisterUsers

urlpatterns = [
    re_path( r'^add/$', RegisterUsers.as_view()),
]