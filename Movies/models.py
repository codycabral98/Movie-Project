from django.db import models

# Create your models here.


class Movie(models.Model):
    movie_id = models.IntegerField(unique=True)
    title = models.CharField(max_length=200)
    imdb_id = models.CharField(max_length=9)

    def __str__(self):
        return self.title
