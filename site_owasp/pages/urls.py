from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_view,name='home'),
    path('profil/',views.profil),
    path('flag',views.flag),
    # path('demarageChallenge/', view/s.lancerMachine),
]
