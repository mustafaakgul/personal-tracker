"""portfolio URL Configuration

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
from index.views import index,base, basetest

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include("accounts.urls", namespace="accounts")),
    path('exercise/', include("sport.urls", namespace="sport")),
    path('project/', include("project.urls", namespace="project")),
    path('endnode/', include("endnode.urls", namespace="endnode")),

    path('', index.index, name='index'),
    path('base/', base.base, name='base'),
    path('basetest/', basetest.basetest, name='basetest'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)