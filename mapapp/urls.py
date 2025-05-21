from django.urls import path
from .views import index, get_filtered_geojson, get_region_info,get_hospitals,get_schools

urlpatterns = [
    path('', index, name='index'),
    path('api/geojson/', get_filtered_geojson, name='filtered_geojson'),  # Main GeoJSON API 
    path('api/info/', get_region_info, name='region_info'),
    path('api/hospitals/', get_hospitals, name='hospitals'),  # Get hospitals by region
    path('api/schools/', get_schools, name='schools'),  # Get schools by region
      
]