from django.db import models


class Bien(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField()
    ville = models.CharField(max_length=100)
    adresse = models.CharField(max_length=255)
    prix = models.DecimalField(max_digits=12, decimal_places=2)
    surface = models.DecimalField(max_digits=8, decimal_places=2)
    disponible = models.BooleanField(default=True)
    image = models.ImageField(upload_to='biens/', blank=True, null=True)

    def __str__(self):
        return self.titre