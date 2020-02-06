from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum
from  .models import Faktura
from .forms import FakturaForm

# Create your views here.
def test(request):
    texty = 'to jest tekst z views'
    lista = [1, 2, 3, 4]
    faktura = Faktura.objects.all()
    suma = Faktura.objects.all().aggregate(Sum('kwota_netto')).get('kwota_netto__sum', 0.00)

    return render(request, 'test.html', {'text': texty, 'lista': lista, 'faktura': faktura, 'suma': suma })

def nowa_faktura(request):
    form = FakturaForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect(test)

    return render(request, 'nowa_faktura.html', {'form': form})

def edycja_faktury(request, id):
    faktura = get_object_or_404(Faktura, pk=id)
    form = FakturaForm(request.POST or None, request.FILES or None, instance=faktura)

    if form.is_valid():
        form.save()
        return redirect(test)

    return render(request, 'nowa_faktura.html', {'form': form})

def usuwanie_faktury(request, id):
    faktura = get_object_or_404(Faktura, pk=id)

    if request.method == 'POST':
        faktura.delete()
        return redirect(test)
    return render(request, 'potwierdz.html', {'faktura': faktura})


