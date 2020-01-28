from django.urls import path

from . import views

urlpatterns = [
    path('', views.security_miscounfiguration, name='security_miscounfiguration'),

]
