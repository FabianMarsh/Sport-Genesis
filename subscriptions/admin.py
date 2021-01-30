from django.contrib import admin
from .models import Subscriptions, Category

# Register your models here.

class SubscriptionsAdmin(admin.ModelAdmin):
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

admin.site.register(Subscriptions, SubscriptionsAdmin)
admin.site.register(Category, CategoryAdmin)
