from django.db import models

# Create your models here.

class Spell(models.Model):
    name = models.CharField(max_length=200) #Campo de texto com limitação
    description = models.TextField() #Campo de texto sem limitação
    
    def __str__(self):
        return self.name

class Characters(models.Model):
    name = models.CharField(max_length=100)
    house = models.CharField(max_length=100)
    wizard = models.BooleanField()
    species = models.CharField(max_length=100)
    eyesColor = models.CharField(max_length=100)
    hairColor = models.CharField(max_length=100)
    actor = models.CharField(max_length=100)
    imagem = models.TextField()