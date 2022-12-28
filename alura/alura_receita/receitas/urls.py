from django.urls import path
from receitas.views import index, receita, buscar
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', index, name='index'),
    path('<int:receita_id>', receita, name='receita'),
    path('buscar', buscar, name='buscar'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
