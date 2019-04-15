# from django.shortcuts import render

# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

from Movies.models import Movie
from Movies.serializers import MovieSerializer


class MovieFilter(filters.FilterSet):
    class Meta:
        model = Movie
        fields = {
            'title': ['icontains'],
            'imdb_id': ['iexact']
        }


class MovieViewSet(viewsets.ModelViewSet):
    permission_classes = (
        IsAuthenticated,
    )
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    #lookup_field = 'title'
    filter_backends = (DjangoFilterBackend,)
    filterset_class = MovieFilter

    #@action(methods=['get'], detail=False)
    # def get_queryset(self):
    #     return Movie.objects.filter(title='Jumanji')
