from django.contrib import admin
from .models import Products, Category


class ProductsAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "category",
        "price",
        "image",
    )

    ordering = ("price",)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "friendly_name",
        "name",
    )

admin.site.register(Products, ProductsAdmin)
admin.site.register(Category, CategoryAdmin)
