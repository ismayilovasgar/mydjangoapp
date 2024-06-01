from django.contrib import admin
from .models import *

# Register your models here.


class BlogAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "is_active",
        "is_home",
        "slug",
    )
    list_editable = (
        "is_active",
        "is_home",
    )

    search_fields = (
        "title",
        "description",
    )

    # readonly_fields = ("description",)
    readonly_fields = ("slug",)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "slug",
    )

    readonly_fields = ("name",)
    search_fields = ("name",)


admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoryAdmin)
