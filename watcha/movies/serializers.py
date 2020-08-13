from django.conf.urls import url,include
from .models import Information
from rest_framework import serializers

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Information
        fields = ('id', 'title', 'link', 'img_link', 'pubYear', 'userRating', 'director', 'actor', 'summary', 'nation', 'genre')
