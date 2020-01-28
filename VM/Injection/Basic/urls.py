from django.urls import path
from . import views

urlpatterns = [
    path('',views.Basic_attack,name='index'),
]
