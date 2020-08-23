"""djangoproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.hello, name="hello"),
    path('hi/<str:val>', views.hi, name="hi"),
    path('details/<str:name>',views.details),
    path('sample/',views.home, name="homey"),
    path('sample1/<str:name>/', views.home1,name='home1'),
    path('extcss/', views.excr, name="extncss"),
    path('jspcss/',views.jsp, name="jspcss"),
    path('register/', views.reg, name="reg"),
    path('botreg/', views.regi,name="botreg")
]