from django.db import models
from django.contrib.auth.models import User
from biens.models import Bien


class Creneau(models.Model):
    bien = models.ForeignKey(Bien, on_delete=models.CASCADE)
    date = models.DateField()
    heure = models.TimeField()

    def __str__(self):
        return f"{self.bien.titre} - {self.date} {self.heure}"


class Reservation(models.Model):
    creneau = models.ForeignKey(Creneau, on_delete=models.CASCADE)
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    date_reservation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.utilisateur.username} - {self.creneau}"