from django.urls import path
from .views import test
from .views import nowa_faktura, edycja_faktury, usuwanie_faktury


urlpatterns = [

    path('', test),
    path('nowa/', nowa_faktura, name = 'nowa_faktura'),
    path('edycja/<int:id>/', edycja_faktury, name = 'edycja_faktury'),
    path('usuwanie/<int:id>/', usuwanie_faktury, name = 'usuwanie_faktury'),



]
