from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('biens.urls')),

    path('comptes/', include('comptes.urls')),

    path(
        'comptes/connexion/',
        auth_views.LoginView.as_view(
            template_name='comptes/connexion.html'
        ),
        name='connexion'
    ),

    path(
        'comptes/deconnexion/',
        auth_views.LogoutView.as_view(next_page='liste'),
        name='deconnexion'
    ),

    path(
        'reservations/',
        include('reservations.urls')
    ),
]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )