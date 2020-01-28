from django.urls import path

from . import views

urlpatterns = [
    path('', views.sensitive_data_exposure, name='sensitive_data_exposure'),

]
