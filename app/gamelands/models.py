from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 

class Games(models.Model):
    game_name = models.CharField(max_length=100)
    release_year = models.IntegerField( 
    null = True,
    blank = True,
    validators = [
        MinValueValidator(1980),
        MaxValueValidator(2026),
                  ]
    )
    metacritic_score = models.IntegerField(
    null = True,
    blank = True,
    validators=[
        MinValueValidator(1),
        MaxValueValidator(100)
        ]
    )
    developers = models.CharField(max_length=100,
    null = True,
    blank = True)
    howlongtobeat = models.IntegerField(
    null = True,
    blank = True)
    image = models.CharField(max_length=40,
    null = True,
    blank = True
    )
    def __str__(self) -> str:
        return f' {self.game_name}'
class User(models.Model):
    ID = models.IntegerField
    username = models.CharField(max_length=40)
    Email = models.EmailField()
    def __str__(self):
        return f'{self.username} {self.Email}'

class Table(models.Model):
    id = models.IntegerField
    name = models.CharField(max_length=20, null= True)
    username = models.CharField(max_length=20, null= True)
    def __str__(self):
        return f'{self.name} {self.username}'
    

# Create your models here.
