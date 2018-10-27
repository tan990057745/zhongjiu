from django.conf.urls import url

from myapp import views

urlpatterns = [
    url('^$', views.index, name='index'),
    url('^register/$', views.register, name='register'),
    url('^login/$', views.login, name='login'),
    url('^verifycode/$', views.verifycode, name='verifycode'),
]
