from django.forms import ModelForm
from .models import Faktura
class FakturaForm(ModelForm):
    class Meta:
        model = Faktura
        fields = ['numer', 'nazwa', 'data_wystawienia', 'kwota_netto', 'vat', 'miejsce', 'plik']
