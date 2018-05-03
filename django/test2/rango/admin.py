from django.contrib import admin
from .models import Category, Page
from rango.models import UserProfile


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


class PageAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "url")


admin.site.register(Page, PageAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site .register(UserProfile)