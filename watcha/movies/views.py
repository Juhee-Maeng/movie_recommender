from django.shortcuts import render
from rest_framework import viewsets, generics
from .models import Information
from .serializers import MovieSerializer

# Create your views here.
class MovieList(generics.ListCreateAPIView):
    queryset = Information.objects.all()
    serializer_class = MovieSerializer
    name = "movie-list"


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Information.objects.all()
    serializer_class = MovieSerializer
    name = "movie-view"
