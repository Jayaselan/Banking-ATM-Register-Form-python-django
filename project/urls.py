"""project URL Configuration

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
from application import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('create', views.create),
    path('created', views.created),
    path('index', views.index),
    path('atm', views.atm),
    path('saving', views.saving),
    path('wm', views.wm),
    path('get_money', views.get_money),
    path('mini_statement', views.mini_statement),
    path('balance', views.balance),
    path('enq', views.enq),
    path('card', views.card),
    path('contact', views.contact),
    path('track', views.track),
    path('about', views.about),

]
