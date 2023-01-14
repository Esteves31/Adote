from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required

def new_pet(request):
    return HttpResponse('Estou em novo_pet')