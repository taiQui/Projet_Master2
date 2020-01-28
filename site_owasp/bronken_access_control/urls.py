from django.urls import path

from . import views

urlpatterns = [
    path('', views.bronken_access_control, name='bronken_access_control'),

]
