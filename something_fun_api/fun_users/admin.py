from django.contrib import admin
from fun_users.models import User
from import_export.admin import ImportExportModelAdmin

# Register your models here.


class UserAdmin(ImportExportModelAdmin):
    pass

admin.site.register(User, UserAdmin)
