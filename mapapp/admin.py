
from django.contrib import admin
from .models import School, Hospital, RegionInfo

# Existing RegionInfo Admin Panel
@admin.register(RegionInfo)
class RegionInfoAdmin(admin.ModelAdmin):
    list_display = ('state', 'district', 'taluk')
    search_fields = ('state', 'district', 'taluk')


# School Admin Panel
class SchoolAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'latitude', 'longitude', 'region']
    search_fields = ['name', 'address', 'region__taluk']
    list_filter = ['region']


# Hospital Admin Panel
class HospitalAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'latitude', 'longitude', 'region']
    search_fields = ['name', 'address', 'region__taluk']
    list_filter = ['region']



# Register models in admin panel
admin.site.register(School, SchoolAdmin)
admin.site.register(Hospital, HospitalAdmin)
