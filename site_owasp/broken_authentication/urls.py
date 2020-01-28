from django.urls import path

from . import views

urlpatterns = [
    path('', views.broken_authentication, name='broken_authentication'),

]
