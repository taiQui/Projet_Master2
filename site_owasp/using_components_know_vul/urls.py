from django.urls import path

from . import views

urlpatterns = [
    path('', views.using_components_know_vul, name='using_components_know_vul'),

]
