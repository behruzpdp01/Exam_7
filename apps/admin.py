from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from apps.models import People


@admin.register(People)
class PeopleAdmin(admin.ModelAdmin):
    pass