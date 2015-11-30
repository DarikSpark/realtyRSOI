from django.conf.urls import url
from . import views

urlpatterns = [
    #url(r'^$', views.ExampleView.as_view()),
    url(r'^$', views.SheduleList.as_view()),
    #url(r'^user/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
]
