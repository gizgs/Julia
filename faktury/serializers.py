from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Faktura


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email',]

class FakturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faktura
        fields = ['id', 'numer', 'nazwa', 'data_wystawienia', 'kwota_netto', 'vat', 'miejsce', 'plik']


