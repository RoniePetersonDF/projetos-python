from django.urls import path
from pessoas.views import index

urlpatterns = [
    path('', index, name='pessoas'),
]


