from django.contrib import admin
from fun_lists.models import Genre, OTT, Movie
from import_export.admin import ImportExportModelAdmin

# Register your models here.


class GenreAdmin(ImportExportModelAdmin):
    list_display = ["name"]
    list_filter = ["name"]


class OTTAdmin(ImportExportModelAdmin):
    list_display = ["name"]
    list_filter = ["name"]


class MovieAdmin(ImportExportModelAdmin):
    list_display = ["name"]
    list_filter = ["name"]


admin.site.register(Movie, MovieAdmin)
admin.site.register(OTT, OTTAdmin)
admin.site.register(Genre, GenreAdmin)
