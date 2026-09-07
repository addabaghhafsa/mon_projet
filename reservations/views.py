from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from .models import Creneau, Reservation


def liste_creneaux(request):
    ids_reserves = Reservation.objects.values_list('creneau_id', flat=True)
    creneaux = Creneau.objects.exclude(id__in=ids_reserves)
    return render(request, 'reservations/liste.html', {'creneaux': creneaux})


@login_required
def reserver(request, creneau_id):
    creneau = Creneau.objects.get(id=creneau_id)
    if not Reservation.objects.filter(creneau=creneau).exists():
        Reservation.objects.create(creneau=creneau, utilisateur=request.user)
        send_mail(
            'Confirmation de réservation',
            f'Votre visite pour {creneau.bien.titre} le {creneau.date} est confirmée.',
            'addabaghhafsaa@gmail.com',
            [request.user.email],
        )
    return redirect('liste_creneaux')


@login_required
def mes_reservations(request):
    reservations = Reservation.objects.filter(utilisateur=request.user)
    return render(request, 'reservations/mes_reservations.html', {'reservations': reservations})


@login_required
def annuler(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id, utilisateur=request.user)
    reservation.delete()
    return redirect('mes_reservations')