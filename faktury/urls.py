from django.urls import path
from .views import nowa_faktura, edycja_faktury, usuwanie_faktury, nowe_miejsce




# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.



urlpatterns = [
    path('nowa/', nowa_faktura, name = 'nowa_faktura'),
    path('edycja/<int:id>/', edycja_faktury, name = 'edycja_faktury'),
    path('usuwanie/<int:id>/', usuwanie_faktury, name = 'usuwanie_faktury'),
    path('nowe_miejsce/', nowe_miejsce, name = 'nowe_miejsce'),

]
