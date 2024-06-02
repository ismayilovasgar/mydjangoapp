from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe

# Register your models here.


class BlogAdmin(admin.ModelAdmin):
    list_display = (
        # "id",
        "title",
        "is_active",
        "is_home",
        "slug",
        # "category_id",
        "selected_categories",
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
    list_filter = ("is_active", "categories")

    def selected_categories(self, obj):
        html = "<ul>"
        for category in obj.categories.all():

            html += "<li>" + category.name + "</li>"
        html += "</ul>"
        return mark_safe(html)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "slug",
    )

    readonly_fields = ("name",)
    search_fields = ("name",)


admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoryAdmin)
