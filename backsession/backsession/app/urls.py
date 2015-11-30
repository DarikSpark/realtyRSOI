from django.conf.urls import url
from . import views as views1
from rest_framework.authtoken import views as views2

urlpatterns = [
    url(r'^$', views1.ExampleView.as_view()),
    url(r'^register/$', views1.Register.as_view()),
    url(r'^login/$', views2.obtain_auth_token),
    url(r'^check/$', views1.Check.as_view()),
    url(r'^logged-user/$', views1.LoggedUser.as_view()),
]
