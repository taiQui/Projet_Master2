from django.urls import path

from . import views

urlpatterns = [
    path('', views.insecure_deserialization, name='insecure_deserialization'),

]
