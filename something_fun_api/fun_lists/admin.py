from django.contrib import admin
from fun_lists.models import Genre, OTT, Movie, Series, List
from import_export.admin import ImportExportModelAdmin
from django.contrib.contenttypes.models import ContentType

# Register your models here.


class GenreAdmin(ImportExportModelAdmin):
    list_display = ["name"]
    list_filter = ["name"]


class OTTAdmin(ImportExportModelAdmin):
    list_display = ["name"]
    list_filter = ["name"]


class MovieAdmin(ImportExportModelAdmin):
    list_display = ["name", "genre", "display_ott"]
    list_filter = ["name", "genre"]

    @admin.display(description="OTT Platforms")
    def display_ott(self, obj):
        return ", ".join([item.name for item in obj.ott_platforms.all()])


class SeriesAdmin(ImportExportModelAdmin):
    list_display = ["name", "genre", "display_ott"]
    list_filter = ["name", "genre"]

    @admin.display(description="OTT Platforms")
    def display_ott(self, obj):
        return ", ".join([item.name for item in obj.ott_platforms.all()])

class ListAdmin(ImportExportModelAdmin):
    list_display = ["content_type", "object_id", "content_object"]

    def _init_(self, *args, **kwargs):
        super()._init_(*args, **kwargs)
        allowed_models = [Movie, Series]
        self.fields['content_type'].queryset = ContentType.objects.filter(model__in=[m._meta.model_name for m in allowed_models])


admin.site.register(Movie, MovieAdmin)
admin.site.register(Series, SeriesAdmin)
admin.site.register(OTT, OTTAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(List, ListAdmin)
