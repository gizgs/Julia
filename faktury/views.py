from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum
from  .models import Faktura
from .forms import FakturaForm, MiejsceForm
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User

# Create your views here.

@login_required
def main(request):
    user1 = request.user.id
    if user1 == 1:
        faktura = Faktura.objects.all()
        sumaN = Faktura.objects.all().aggregate(Sum('kwota_netto')).get('kwota_netto__sum', 0.00)
        return render(request, 'main.html', {'faktura': faktura, 'sumaN': sumaN})
    else:
        faktura = Faktura.objects.filter(id_user = request.user.id)


        return render(request, 'main.html', {'faktura': faktura})

@login_required
def nowa_faktura(request):
    form = FakturaForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        faktura = form.save(commit=False)
        faktura.id_user = request.user
        form.save()
        return redirect(main)

    return render(request, 'nowa_faktura.html', {'form': form})


@login_required
def edycja_faktury(request, id):
    faktura = get_object_or_404(Faktura, pk=id)
    form = FakturaForm(request.POST or None, request.FILES or None, instance=faktura)
    if form.is_valid():
        form.save()
        return redirect(main)
    return render(request, 'nowa_faktura.html', {'form': form})


@login_required
def usuwanie_faktury(request, id):
    faktura = get_object_or_404(Faktura, pk=id)
    if request.method == 'POST':
        faktura.delete()
        return redirect(main)
    return render(request, 'potwierdz.html', {'faktura': faktura})


@login_required
def nowe_miejsce(request):

    form = MiejsceForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect(main)

    return render(request, 'nowe_miejsce.html', {'form': form})

