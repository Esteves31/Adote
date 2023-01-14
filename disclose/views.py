from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def new_pet(request):
    return HttpResponse('Estou em novo_pet')