from django.shortcuts import render, redirect
from disclose.models import Pet, Breed
from django.contrib import messages
from django.contrib.messages import constants
from .models import Adoption_application
from datetime import datetime

def list_pets(request):
    if request.method == "GET":
        pets = Pet.objects.filter(status='P')
        breeds = Breed.objects.all()

        city = request.GET.get('cidade')
        breed_filter = request.GET.get('raca')

        if city:
            pets = pets.filter(city__icontains=city)

        if breed_filter:
            pets = pets.filter(breed__id=breed_filter)
            breed_filter = Breed.objects.get(id=breed_filter)
        return render(request, 'list_pets.html', {'pets': pets, 'breeds': breeds, 'city': city, 'breed_filter': breed_filter})
    
def adoption_application(request, id_pet):
    pet = Pet.objects.filter(id=id_pet).filter(status="P")

    if not pet.exists():
        messages.add_message(request, constants.ERROR, 'Ops, esse pet já foi adotado :)')
        return redirect('/adotar')

    requests = Adoption_application(pet=pet.first(),
                                   user=request.user,
                                   date=datetime.now())

    requests.save()

    messages.add_message(request, constants.SUCCESS, 'Pedido de adoção realizado, você receberá um e-mail caso ele seja aprovado.')
    return redirect('/adotar')
