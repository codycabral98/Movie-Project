from django.contrib import admin


# Register your models here.
from Movies.models import Movie

admin.site.register(Movie)
