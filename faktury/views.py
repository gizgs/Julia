from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Sum

from  .models import Faktura

# Create your views here.
def test(request):
    texty = 'to jest tekst z views'
    lista = [1, 2, 3, 4]
    faktura = Faktura.objects.all()
    suma = Faktura.objects.all().aggregate(Sum('kwota_netto')).get('kwota_netto__sum', 0.00)

    return render(request, 'test.html', {'text': texty, 'lista': lista, 'faktura': faktura, 'suma': suma })
