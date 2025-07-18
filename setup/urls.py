from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from avaliacao_docente import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("avaliacao_docente.urls")),
    path("registro/", views.RegistrarUsuarioView.as_view(), name="registro"),
    path("accounts/", include("django.contrib.auth.urls")),  # Para autenticação
]

# Servir arquivos estáticos em desenvolvimento
if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0]
    )
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    # Para produção, servir arquivos estáticos coletados
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
