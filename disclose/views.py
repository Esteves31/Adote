from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Tag, Breed, Pet
from django.contrib import messages
from django.contrib.messages import constants
from django.shortcuts import redirect
from adopt.models import Adoption_application
from django.views.decorators.csrf import csrf_exempt

@login_required
def new_pet(request):
    if request.method == "GET":
        tags = Tag.objects.all()
        breeds = Breed.objects.all()
        return render(request, 'new_pet.html', {'tags': tags, "breeds": breeds})
    elif request.method == "POST":
        photo = request.FILES.get('foto')
        name = request.POST.get('nome')
        description = request.POST.get('descricao')
        state = request.POST.get('estado')
        city = request.POST.get('cidade')
        phone = request.POST.get('telefone')
        tags = request.POST.getlist('tags')
        breed = request.POST.get('raca')

        pet = Pet(
            user = request.user,
            photo = photo,
            pet_name = name,
            description = description,
            state = state,
            city = city,
            number_phone = phone,
            breed_id = breed,
        )

        pet.save()

        for tag_id in tags:
            tag = Tag.objects.get(id=tag_id)
            pet.tags.add(tag)
        
        pet.save()

        return redirect('/divulgar/seus_pets/')

@login_required
def your_pets(request):
    if request.method == "GET":
        pets = Pet.objects.filter(user=request.user)
        return render(request, 'your_pets.html', {'pets': pets})

@login_required
def remove_pet(request, id):
    pet = Pet.objects.get(id=id)
    if not pet.user == request.user:
        messages.add_message(request, constants.ERROR, 'Opa, você não é dono desse pet')
        return redirect('/divulgar/seus_pets/')
    pet.delete()

    messages.add_message(request, constants.SUCCESS, 'O pet foi removido com sucesso!')
    return redirect('/divulgar/seus_pets/')

@login_required
def see_pet(request, id):
    if request.method == "GET":
        pet = Pet.objects.get(id=id)
        return render(request, 'see_pet.html', {'pet': pet})

@login_required
def see_adopt_application(request):
    if request.method == "GET":
        requests = Adoption_application.objects.filter(user=request.user).filter(status="AG")
        return render(request, 'see_adopt_application.html', {'requests': requests})

@login_required
def dashboard(request):
    if request.method ==  "GET":
        return render(request, 'dashboard.html')

@csrf_exempt
def adoption_by_breed_api(request):
    breeds = Breed.objects.all()
    number_adoptions = []

    for breed in breeds:
        adopts = Adoption_application.objects.filter(pet__breed=breed).count()
        number_adoptions.append(adopts)

    breeds = [breed.breed for breed in breeds]
    data = {'number_adoptions': number_adoptions,
            'labels': breeds}
    return JsonResponse(data)