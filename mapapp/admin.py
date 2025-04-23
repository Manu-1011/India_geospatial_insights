from django.contrib import admin
from .models import RegionInfo

@admin.register(RegionInfo)
class RegionInfoAdmin(admin.ModelAdmin):
    list_display = ('state', 'district', 'taluk')
    search_fields = ('state', 'district', 'taluk')
