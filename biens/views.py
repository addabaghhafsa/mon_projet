from django.shortcuts import render
from .models import Bien
from django.contrib.admin.views.decorators import staff_member_required
from reservations.models import Reservation, Creneau


def liste_biens(request):
    biens = Bien.objects.all()
    return render(request, 'biens/liste.html', {'biens': biens})


@staff_member_required
def dashboard(request):
    context = {
        'total_biens': Bien.objects.count(),
        'total_reservations': Reservation.objects.count(),
        'total_creneaux': Creneau.objects.count(),
    }
    return render(request, 'biens/dashboard.html', context)