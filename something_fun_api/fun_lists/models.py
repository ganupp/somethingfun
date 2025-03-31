from django.db import models

# Create your models here.


class Genre(models.Model):
    name = models.CharField(max_length=255)


class OTT(models.Model):
    name = models.CharField(max_length=255)


class Movie(models.Model):
    name = models.CharField(max_length=1000)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    ott_platforms = models.ManyToManyField(OTT, null=True, blank=True)
