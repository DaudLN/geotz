from django.contrib import admin

from .models import District, Region, Ward


# Register your models here.
@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ["name"]


@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    autocomplete_fields = ["region"]


@admin.register(Ward)
class WardAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
