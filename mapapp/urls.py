from django.urls import path
from .views import index, get_filtered_geojson, get_colored_states,get_region_info

urlpatterns = [
    path('', index, name='index'),
    path('api/geojson/', get_filtered_geojson, name='filtered_geojson'),  # Main GeoJSON API
    path('api/get_colors/', get_colored_states, name='get_colors'), 
    path('api/info/', get_region_info, name='region_info'),
      
]