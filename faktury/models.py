from decimal import Decimal

from django.db import models
# Create your models here.
class Faktura(models.Model):
    miejsca = [
        ('Żagań', 'Żagań'),
        ('Krasiczyn', 'Krasiczyn'),
    ]

    vaty = {
        (Decimal("0.23"), '23'),

    }

    numer = models.CharField(max_length=100)
    nazwa = models.CharField(max_length=100)
    data_wystawienia = models.DateField()
    kwota_netto = models.DecimalField(decimal_places=2, max_digits=10)
    vat = models.DecimalField(decimal_places=2, max_digits=10, choices=vaty)
    miejsce = models.CharField(choices=miejsca, max_length=30)
    plik = models.FileField()

    def __str__(self):
        return self.nazwa
