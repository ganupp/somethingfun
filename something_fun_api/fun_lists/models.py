from django.db import models

# Create your models here.


class Genre(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class OTT(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Movie(models.Model):
    name = models.CharField(max_length=1000)
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True, blank=True)
    ott_platforms = models.ManyToManyField(OTT, blank=True)

    def __str__(self):
        return self.name


class Series(models.Model):
    name = models.CharField(max_length=1000)
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True, blank=True)
    ott = models.ManyToManyField(OTT, blank=True)

    def __str__(self):
        return self.name
