from django.db import models
# Create your models here.

class Information(models.Model):
    id = models.AutoField(primary_key = True)
    title = models.CharField(max_length=50)
    link = models.CharField(max_length=100)
    img_link = models.CharField(max_length=100)
    pubYear = models.IntegerField()
    userRating = models.FloatField()
    director = models.CharField(max_length=50)
    actor = models.TextField()
    summary = models.TextField()
    nation = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)

    def __str__(self):
        return self.title

    # specify table name
    class Meta:
        db_table = 'movie_information'
