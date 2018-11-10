from django.conf.urls import url

from myapp import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.login, name='login'),                        #登录
    url(r'^logout/$', views.logout, name='logout'),                     #登出
    # url(r'^market/(\d+)/(\d+)/(\d+)/(\d+)/(\d+)/$', views.market, name='market'),
    url(r'^market/$', views.market, name='market'),
    url(r'^verifycode/$', views.verifycode, name='verifycode'),
    url(r'^verifycode/\d+/$', views.verifycode),                #验证码刷新
    url(r'^shoppingCart/$', views.shoppingCart, name='shoppingCart'),

    url(r'^checkVerifyCode/$', views.checkVerifyCode, name='checkVerifyCode'),    #校验码验证
    url(r'^checkaccount/$', views.checkaccount, name='checkaccount'),


]
