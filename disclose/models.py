from django.db import models
from django.contrib.auth.models import User

class Breed(models.Model):
    breed = models.CharField(max_length=50)

    def __str__(self):
        return self.breed

class Tag(models.Model):
    tag = models.CharField(max_length=100)

    def __str__(self):
        return self.tag

class Pet(models.Model):
    choice_status = (('P', 'Para adoção'),
                     ('A', 'Adotado'))
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    photo = models.ImageField(upload_to="pets_photos")
    pet_name = models.CharField(max_length=100)
    description = models.TextField()
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    number_phone = models.CharField(max_length=14)
    tags = models.ManyToManyField(Tag)
    breed = models.ForeignKey(Breed, on_delete=models.DO_NOTHING)
    status = models.CharField(max_length=1, choices=choice_status)

    def __str__(self):
        return self.pet_name