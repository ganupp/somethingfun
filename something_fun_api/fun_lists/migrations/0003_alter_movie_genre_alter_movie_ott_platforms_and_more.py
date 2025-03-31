# Generated by Django 5.1.7 on 2025-03-31 12:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("fun_lists", "0002_series"),
    ]

    operations = [
        migrations.AlterField(
            model_name="movie",
            name="genre",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="fun_lists.genre",
            ),
        ),
        migrations.AlterField(
            model_name="movie",
            name="ott_platforms",
            field=models.ManyToManyField(blank=True, to="fun_lists.ott"),
        ),
        migrations.AlterField(
            model_name="series",
            name="genre",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="fun_lists.genre",
            ),
        ),
        migrations.AlterField(
            model_name="series",
            name="ott",
            field=models.ManyToManyField(blank=True, to="fun_lists.ott"),
        ),
    ]
