from django.urls import path, include, re_path


from Profile.views import ProfileTable,ProfileTableDetail, UserProfileData


urlpatterns = [
    re_path( r'^perfil$', ProfileTable.as_view()),
    re_path( r'^lista_perfil/(?P<pk>\d+)/$', ProfileTableDetail.as_view()),
    re_path(r'^data/(?P<pk>\d+)$', UserProfileData.as_view()),
]