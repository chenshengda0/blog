#coding:utf-8
"""olnote URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from blog import views
from blog import models

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r"^discuss/$",views.discuss),#,{'template':'user/comment.html'}
    url(r"^discuss/(?P<metd>\w+)/(?P<cid>\d+)/$",views.discuss_mailto),#,{'template':'user/comment.html'}
    url(r"^discuss/$",views.discuss),#,{'template':'user/comment.html'}
    url(r'^$',views.MyView.as_view()),
    url(r"^tags/(?P<tag>t_\d+)/$",views.MyView.as_view()),
    url(r"^(?P<conts>\w+?)/(?P<temp>.+?)/(?P<lid>.+?)/",views.MyView.as_view()),
    url(r"^register/$",views.register,{'template':'user/register.html'}),
    url(r"^login/$",views.login,{'template':'user/login.html'}),
    url(r"^forget/(?P<username>.+?)/$",views.forget,{'template':"user/forget.html"}),
    url(r"^comment/$",views.comment),

]
