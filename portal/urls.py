"""portal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from userprofile import views as upv

from portal import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/profile/', upv.userprofile),
    path('', views.main),

    path('games/', views.games),
  #  path('games/1', views.game),
   # path('games/<int:id>',views.game),
    path('games/1',views.game1),
    path('games/2',views.game2),
    path('games/3',views.game3),



    path('accounts/login/', views.login),
    path('accounts/auth/', views.auth_view),
    path('accounts/logout/', views.logout),
    path('accounts/loggedin/', views.loggedin),
    path('accounts/invalid/', views.invalid_login),


    path('accounts/create_user/', views.create_user),
    path('accounts/create_user_success/', views.create_user_success),

]
