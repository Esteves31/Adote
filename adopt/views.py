from django.shortcuts import render
from disclose.models import Pet, Breed

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
    
