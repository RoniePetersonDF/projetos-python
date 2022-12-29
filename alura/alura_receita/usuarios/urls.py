from django.urls import path
from usuarios.views import cadastro, login, logout, dashboard, cria_receita


urlpatterns = [
    path('cadastro/', cadastro, name='cadastro'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('dashboard/', dashboard, name='dashboard'),
    path('cria/receita/', cria_receita, name='cria_receita'),

]
