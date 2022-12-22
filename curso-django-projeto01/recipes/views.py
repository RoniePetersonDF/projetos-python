from django.shortcuts import render
from django.http import HttpResponse


def home(requet):
    return HttpResponse('HOME') 

def contato(requet):
    return HttpResponse('CONTATO') 

def sobre(requet):
    return HttpResponse('SOBRE') 