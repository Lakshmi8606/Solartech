"""
URL configuration for SolarEnergy project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path,include

from django.conf.urls.static import static
from django.conf import settings
from django.shortcuts import redirect


urlpatterns = [
     path('', lambda request: redirect('/Guest/index/')),
    path('admin/', admin.site.urls),
    path('webbasics/',include('Basics.urls')),
    path('Admin/',include('Admin.urls')),
    path('Guest/',include('Guest.urls')),
    path('Test/',include('Test.urls')),
    path('User/',include('User.urls')),
    path('Sp/',include('Sp.urls')),


]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                   document_root=settings.MEDIA_ROOT)
