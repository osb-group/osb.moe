"""osb URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include, url
from django.contrib import admin
from main.views import HomePageView

urlpatterns = [
    url(r'^twintails/', admin.site.urls),
    url(r'^api/', include('osb_api.urls')),
    url(r'^showcase/', include('showcase.urls')),
    url(r'^user/', include('main.urls_user')),
    url(r'^learn/', include('sphinxdoc.urls')),
    url(r'^pages/', include('django.contrib.flatpages.urls')),
    url(r'^$', HomePageView.as_view(), name='index'),
    url(r'^photologue/', include('photologue.urls', namespace='photologue')),
]
