from django.shortcuts import render
from django.http import HttpResponse


def home(requet):
    return render(requet, 'recipes/home.html') 

def contato(requet):
    return HttpResponse('CONTATO') 

def sobre(requet):
    return HttpResponse('SOBRE') 