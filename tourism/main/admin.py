from django.contrib import admin

from .models import Travel, Region


class TravelAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'built_at',
        'updated_at'
    )
    list_display_links = (
        'id',
        'name'
    )
    search_fields = (
        'name',
        'content'
    )
    list_filter = (
        'region',
    )


class RegionAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name'
    )
    list_display_links = (
        'id',
        'name'
    )
    search_fields = (
        'name',
    )


admin.site.register(Travel, TravelAdmin)
admin.site.register(Region, RegionAdmin)

