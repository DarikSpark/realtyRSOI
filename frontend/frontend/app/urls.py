from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^flat/$', views.flat, name='flat'),
    url(r'^flat/(?P<pk>[0-9]+)/$', views.flat_detail, name='flat_detail'),
    url(r'^flat/my/$', views.flat_my, name='flat_my'),
    url(r'^flat/my/(?P<pk>[0-9]+)/$', views.flat_my_detail, name='flat_my_detail'),
    url(r'^flat/my/create/$', views.flat_my_create, name='flat_my_create'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^is_logged/$', views.is_logged),
    url(r'^flat/(?P<pk>[0-9]+)/shedule$', views.shedule, name='shedule'),
    url(r'^flat/(?P<pk>[0-9]+)/reservation', views.reservation, name='reservation'),
]
