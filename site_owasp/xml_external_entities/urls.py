from django.urls import path

from . import views

urlpatterns = [
    path('', views.xml_external_entities, name='xml_external_entities'),

]
