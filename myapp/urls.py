from django.conf.urls import url

from myapp import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.login, name='login'),
    url(r'^market/(\d+)/(\d+)/(\d+)/(\d+)/(\d+)/$', views.market, name='market'),
    url(r'^verifycode/\d+/$', views.verifycode, name='verifycode'),
    url(r'^shoppingCart/$', views.shoppingCart, name='shoppingCart'),
    url(r'^test/$', views.test, name='test'),

]
