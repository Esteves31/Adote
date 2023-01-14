from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Tag, Breed, Pet

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

        return HttpResponse("teste")

@login_required
def your_pets(request):
    if request.method == "GET":
        pets = Pet.objects.filter(user=request.user)
        return render(request, 'your_pets.html', {'pets': pets})