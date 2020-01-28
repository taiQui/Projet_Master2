from django.urls import path

from . import views

urlpatterns = [
    path('', views.insufficient_log, name='insufficient_log'),

]
