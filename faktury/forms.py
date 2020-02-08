from django.forms import ModelForm
from .models import Faktura, Miejsce

class FakturaForm(ModelForm):
    class Meta:
        model = Faktura
        fields = ['numer', 'nazwa', 'data_wystawienia', 'kwota_netto', 'vat', 'miejsce', 'plik']
        exclude = ['id_user']

class MiejsceForm(ModelForm):
    class Meta:
        model = Miejsce
        fields = ['miejsce']

