from django.db import models

class Breed(models.Model):
    breed = models.CharField(max_length=50)

    def __str__(self):
        return self.breed
