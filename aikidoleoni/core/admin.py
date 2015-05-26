from django.contrib import admin
from aikidoleoni.core.models import Page


class PageAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Page, PageAdmin)
# Register your models here.
