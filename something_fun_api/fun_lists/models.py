from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import fields
from fun_users.models import User


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
    ott_platforms = models.ManyToManyField(OTT, blank=True)

    def __str__(self):
        return self.name


class List(models.Model):
    allowed_models = ["fun_lists.Movie", "fun_lists.Series"]

    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        limit_choices_to={
            "model__in": [m.split(".")[1].lower() for m in allowed_models],
            "app_label__in": list(set(m.split(".")[0] for m in allowed_models)),
        },
    )
    object_id = models.PositiveIntegerField()
    content_object = fields.GenericForeignKey("content_type", "object_id")
