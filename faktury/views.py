from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum
from  .models import Faktura
from .forms import FakturaForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def login(request):
 return render(request, 'login.html')

@login_required
def test(request):
    faktura = Faktura.objects.all()
    suma = Faktura.objects.all().aggregate(Sum('kwota_netto')).get('kwota_netto__sum', 0.00)

    return render(request, 'test.html', {'faktura': faktura, 'suma': suma,})
@login_required
def nowa_faktura(request):
    form = FakturaForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect(test)

    return render(request, 'nowa_faktura.html', {'form': form})
@login_required
def edycja_faktury(request, id):
    faktura = get_object_or_404(Faktura, pk=id)
    form = FakturaForm(request.POST or None, request.FILES or None, instance=faktura)

    if form.is_valid():
        form.save()
        return redirect(test)

    return render(request, 'nowa_faktura.html', {'form': form})
@login_required
def usuwanie_faktury(request, id):
    faktura = get_object_or_404(Faktura, pk=id)

    if request.method == 'POST':
        faktura.delete()
        return redirect(test)
    return render(request, 'potwierdz.html', {'faktura': faktura})


