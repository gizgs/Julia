from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from  django.contrib.auth import views as auth_views
from faktury.views import login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('faktury/', include('faktury.urls')),
    path('accounts/', include('django.contrib.auth.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
