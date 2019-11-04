"""socialsimple URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include,path
from django.contrib.auth.views import LoginView,LogoutView
from . import views


app_name = 'accounts'

urlpatterns = [
    # default is registration/login.html
    #url(r'^login/$', auth_views.login, name='login'),
    path('login', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    # path('accounts/logout',LogoutView.as_view(template_name='accounts/index.html'), name='logout',kwargs={'next_page':'/'}),
    path('logout', LogoutView.as_view(), name='logout'),
    # by default go back to  homepage
    path('', include('django.contrib.auth.urls')), #Q: login not work unless put this line in the same file with login

    # creation sign up page
    path('signup', views.SignUp.as_view(), name='signup'),
]
