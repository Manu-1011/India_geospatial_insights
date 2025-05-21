import os
import json
from django.conf import settings
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_GET
from .models import  RegionInfo, Hospital, School

def index(request):
    return render(request, 'index.html')


@require_GET
def get_filtered_geojson(request):
    level = request.GET.get('level', 'state')  # 'state', 'district', 'city'
    selected_state = request.GET.get('state')
    selected_district = request.GET.get('district')

    geojson_path = os.path.join(settings.BASE_DIR, 'static', 'geojson', 'india_city.geojson')
    if not os.path.exists(geojson_path):
        return JsonResponse({'error': 'GeoJSON file not found'}, status=404)

    with open(geojson_path, 'r', encoding='utf-8') as f:
        geo_data = json.load(f)

    region_data = RegionInfo.objects.all()
    region_lookup = {
        (r.state.strip(), r.district.strip(), r.taluk.strip()): {
            "population": r.population,
            "literacy_rate": r.literacy_rate,
            "health_centers": r.health_centers,
            "schools": r.schools,
            "famous_for": r.famous_for
        }
        for r in region_data
    }

    filtered_features = []

    for feature in geo_data.get('features', []):
        props = feature.get('properties', {})
        state_name = props.get('NAME_1', '').strip()
        district_name = props.get('NAME_2', '').strip()
        taluk_name = props.get('NAME_3', '').strip()

        key = (state_name, district_name, taluk_name)
        region_info = region_lookup.get(key)

        if region_info:
            props.update(region_info)

        if level == 'state':
            if not selected_state or state_name == selected_state:
                filtered_features.append(feature)

        elif level == 'district':
            if state_name == selected_state:
                if not selected_district or district_name == selected_district:
                    filtered_features.append(feature)

        elif level == 'city':
            if district_name == selected_district:
                filtered_features.append(feature)

    return JsonResponse({
        'type': 'FeatureCollection',
        'features': filtered_features
    })



@require_GET
def get_region_info(request):
    state = request.GET.get("state", "").strip()
    district = request.GET.get("district", "").strip()
    taluk = request.GET.get("taluk", "").strip()

    try:
        region = RegionInfo.objects.get(state=state, district=district, taluk=taluk)
        return JsonResponse({
            "state": region.state,
            "district": region.district,
            "taluk": region.taluk,
            "population": region.population,
            "literacy_rate": region.literacy_rate,
            "health_centers": region.health_centers,
            "schools": region.schools,
            "famous_for": region.famous_for
        })
    except RegionInfo.DoesNotExist:
        return JsonResponse({
            "state": state,
            "district": district,
            "taluk": taluk,
            "info": "No data found in database."
        })


@require_GET
def get_schools(request):
    state = request.GET.get("state", "").strip()
    district = request.GET.get("district", "").strip()
    taluk = request.GET.get("taluk", "").strip()

    try:
        region = RegionInfo.objects.get(state=state, district=district, taluk=taluk)
        schools = School.objects.filter(region=region)
        school_data = [{
            'name': school.name,
            'address': school.address,
            'latitude': school.latitude,
            'longitude': school.longitude
        } for school in schools]

        return JsonResponse({"schools": school_data})
    except RegionInfo.DoesNotExist:
        return JsonResponse({"error": "Region not found"})


# Get hospitals for a specific region (state, district, taluk)
@require_GET
def get_hospitals(request):
    state = request.GET.get("state", "").strip()
    district = request.GET.get("district", "").strip()
    taluk = request.GET.get("taluk", "").strip()

    try:
        region = RegionInfo.objects.get(state=state, district=district, taluk=taluk)
        hospitals = Hospital.objects.filter(region=region)
        hospital_data = [{
            'name': hospital.name,
            'address': hospital.address,
            'latitude': hospital.latitude,
            'longitude': hospital.longitude
        } for hospital in hospitals]

        return JsonResponse({"hospitals": hospital_data})
    except RegionInfo.DoesNotExist:
        return JsonResponse({"error": "Region not found"})