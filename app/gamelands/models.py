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
    game_genres = models.CharField(max_length= 200,
    null = True)
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


class Genres(models.Model):
    id = models.IntegerField
    genre = models.CharField(
        max_length=200,
        null= True
    )

class TablesCombined(models.Model):
    game_id = models.IntegerField 
    genre_id = models.IntegerField
    relationship_factor = models.IntegerField


class Profile(models.Model):
    nickname = models.CharField(max_length= 20)
    pfp = models.ImageField(upload_to="profilepics/", blank=True, null=True)
    description = models.CharField(max_length= 240)
    favourite = models.CharField(max_length=50)
# Create your models here.
