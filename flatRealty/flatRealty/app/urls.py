from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.FlatList.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', views.FlatDetail.as_view()),
    url(r'^my/$', views.MyFlatList.as_view()),
    url(r'^my/(?P<pk>[0-9]+)/$', views.MyFlatDetail.as_view()),
    # url(r'^snippets/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view()),
]
