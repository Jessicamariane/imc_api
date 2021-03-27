from django.contrib import admin
from core.models import People


@admin.register(People)
class PeopleAdmin(admin.ModelAdmin):
    pass
