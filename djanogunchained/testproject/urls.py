"""testproject URL Configuration

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
from django.conf.urls.static import static
from django.conf import settings
from tester import views as testerViews
from accountinfo import views as aiViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', testerViews.home, name='home'),
    path('about/', testerViews.about, name ='about'),
    path('movie/', include('tester.urls')),
    path('accountinfo/', include('accountinfo.urls')),
    # path('favorites/', testerViews.favorites, name='favorites'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)