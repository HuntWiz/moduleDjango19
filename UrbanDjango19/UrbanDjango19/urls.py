"""
URL configuration for UrbanDjango19 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from task1.views import Platform, Games, Cart, sign_up_by_html, post_list

urlpatterns = [
    path('news/', post_list),
    path('', sign_up_by_html),
    path('admin/', admin.site.urls),
    path('platform/', Platform.as_view()),
    path('platform/games', Games),
    path('platform/cart', Cart)
]
