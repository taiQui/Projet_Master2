"""site_owasp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import include
<<<<<<< HEAD
<<<<<<< HEAD
from pages.views import home_view,profil

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('faille_1/', include('faille_1.urls')),
    path('', include('pages.urls')),
    path('broken_authentication/', include('broken_authentication.urls')),
    path('bronken_access_control/',include('bronken_access_control.urls')),
    path('insecure_deserialization/',include('insecure_deserialization.urls')),
    path('insufficient_log/',include('insufficient_log.urls')),
    path('security_miscounfiguration',include('security_miscounfiguration.urls')),
    path('sensitive_data_exposure',include('sensitive_data_exposure.urls')),
    path('xml_external_entities',include('xml_external_entities.urls')),
    path('xss',include('xss.urls')),
    path('using_components_know_vul',include('using_components_know_vul.urls'))
=======
=======
>>>>>>> refs/remotes/origin/master
from pages.views import home_view

urlpatterns = [
    path('admin/', admin.site.urls),

    path('accounts/', include('django.contrib.auth.urls')),
    path('faille_1/', include('faille_1.urls')),
    path('', home_view, name='home')
<<<<<<< HEAD
>>>>>>> 37490fcfc9b9789a29ca4709225c286298a7f7bb
=======
>>>>>>> refs/remotes/origin/master

]
