from django.urls import path
from .views import main
from .views import nowa_faktura, edycja_faktury, usuwanie_faktury

from django.urls import include, path
from rest_framework import routers
from .views import UserViewSet, FakturaViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'faktury', FakturaViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.



urlpatterns = [
    path('nowa/', nowa_faktura, name = 'nowa_faktura'),
    path('edycja/<int:id>/', edycja_faktury, name = 'edycja_faktury'),
    path('usuwanie/<int:id>/', usuwanie_faktury, name = 'usuwanie_faktury'),
    path('', include(router.urls)),


]
