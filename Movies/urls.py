from django.urls import path, include
from rest_framework.routers import DefaultRouter

from Movies import views

router = DefaultRouter()
router.register(r'movies', views.MovieViewSet)
#router.register(r'movies/\?title__icontains=(?P<movie_title>\w+)/?$', views.MovieViewSet)
#title__icontains=Toy+Story
urlpatterns = [
    path('', include(router.urls))
]
