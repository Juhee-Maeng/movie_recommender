from django.urls import path

from .views import MovieViewSet, MovieList

urlpatterns = [
    path("", MovieList.as_view(), name = MovieList.name),
    path("viewset/", MovieViewSet.as_view({'get':'list'}), name = MovieViewSet.name),
]
