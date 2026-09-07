from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_biens, name='liste'),
    path('dashboard/', views.dashboard, name='dashboard'),
]