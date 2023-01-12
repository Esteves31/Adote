from django.db import models

class Breed(models.Model):
    breed = models.CharField(max_length=50)

    def __str__(self):
        return self.breed

class Tag(models.Model):
    tag = models.CharField(max_length=100)

    def __str__(self):
        return self.tag
