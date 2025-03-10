from django.contrib import admin
from django.urls import path, include
from django.conf import settings  # Importando o settings para acessar a configuração de mídia
from django.conf.urls.static import static  # Importando para servir arquivos estáticos durante o desenvolvimento

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Sistema_Poly.urls')),
]

# Serve arquivos de mídia durante o desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)