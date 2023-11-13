from django.db import models

# Create your models here.
class Cat(models.Model):

    name = models.CharField(max_length=100)
    
    age = models.IntegerField()

    breed = models.CharField(max_length=100)

    is_adopted = models.BooleanField(default=False)

    image_url = models.CharField(max_length=400, default = "https://cdn2.thecatapi.com/images/FTd8l4EXq.jpg")

    def __str__(self):
        return self.name