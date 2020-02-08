from decimal import Decimal
from django.contrib.auth.models import User
from django.db import models
# Create your models here.
class Miejsce (models.Model):
    miejsce = models.CharField(max_length=100);

    def __str__(self):
        return self.miejsce



class Faktura(models.Model):
    vaty = {
        (Decimal("0.23"), '23'),
        (Decimal("0.08"), '8'),
        (Decimal("0.05"), '5'),
        (Decimal("0.00"), '0'),

    }

    numer = models.CharField(max_length=100)
    nazwa = models.CharField(max_length=100)
    data_wystawienia = models.DateField()
    kwota_netto = models.DecimalField(decimal_places=2, max_digits=10)
    vat = models.DecimalField(decimal_places=2, max_digits=10, choices=vaty)
    miejsce = models.ForeignKey(Miejsce, on_delete=models.CASCADE)
    plik = models.FileField()
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.nazwa
