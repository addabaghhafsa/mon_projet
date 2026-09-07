from django.urls import path
from . import views


urlpatterns = [
    path(
        '',
        views.liste_creneaux,
        name='liste_creneaux'
    ),

    path(
        'reserver/<int:creneau_id>/',
        views.reserver,
        name='reserver'
    ),

    path(
        'mes-reservations/',
        views.mes_reservations,
        name='mes_reservations'
    ),

    path(
        'annuler/<int:reservation_id>/',
        views.annuler,
        name='annuler'
    ),
]