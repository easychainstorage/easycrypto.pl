"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.views.generic import TemplateView
from settings import ADMIN_SITE

urlpatterns = [
    path(ADMIN_SITE, admin.site.urls),
    path('about', TemplateView.as_view(template_name='about/about.html'), name='about'),
    path('', include('ebook.urls', namespace='ebook')),
    path('', include('dictionary.urls', namespace='dictionary')),
    path("", include("news.urls")),  # new
]
