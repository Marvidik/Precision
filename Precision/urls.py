"""Precision URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from exam import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.home,name="home"),
    path('login/',views.log,name='login'),
    path("reginfo",views.exam_reg,name="examreg"),
    path("question/get_score",views.savemscore,name="mscore"),
    path("english/get_score",views.saveescore,name="escore"),
    path('login/user_login/',views.user_login,name='user_login'),
    path('instructions/',views.instruction,name='instruction'),
    path('question/',views.questions,name='questions'),
    path('english/',views.english,name='english'),
    path('demo/',views.demo,name='demo'),
    path("add_contact/",views.contact,name="add_contact"),
]
