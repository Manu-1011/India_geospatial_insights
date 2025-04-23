import json
import random
from django.core.management.base import BaseCommand
from mapapp.models import RegionInfo
from pathlib import Path

class Command(BaseCommand):
    help = 'Seeds RegionInfo table with fake data from india_city.geojson'

    def handle(self, *args, **kwargs):
        file_path = Path('static/geojson/india_city.geojson')  # ✅ Correct path format
        RegionInfo.objects.all().delete()
        self.stdout.write(self.style.WARNING("🗑️ Cleared existing RegionInfo records."))
        if not file_path.exists():
            self.stdout.write(self.style.ERROR(f"❌ File not found: {file_path.resolve()}"))
            return

        with open(file_path, 'r', encoding='utf-8') as f:
            geojson_data = json.load(f)

        features = geojson_data.get('features', [])
        self.stdout.write(self.style.WARNING(f"🌍 Total features found: {len(features)}"))

        created = 0
        for i, feature in enumerate(features, start=1):
            props = feature.get('properties', {})

            # Debug print on first few items
            if i <= 3:
                print(f"🧩 Feature {i}: {props}")

            state = props.get('NAME_1', '').strip()
            district = props.get('NAME_2', '').strip()
            taluk = props.get('NAME_3', '').strip()


            if not (state and district and taluk):
                continue
            if not (state and district and taluk) or 'n.a.' in taluk.lower():
                continue


            # Skip duplicates
            if RegionInfo.objects.filter(state=state, district=district, taluk=taluk).exists():
                continue

            # Generate fake data
            population = random.randint(10000, 500000)
            literacy_rate = round(random.uniform(60.0, 99.9), 2)
            health_centers = random.randint(1, 50)
            schools = random.randint(5, 100)
            famous_for = random.choice([
                "Historical monuments", "Agriculture", "Temples",
                "Tourism", "Handicrafts", "Spices", "Textiles"
            ])

            RegionInfo.objects.create(
                state=state,
                district=district,
                taluk=taluk,
                population=population,
                literacy_rate=literacy_rate,
                health_centers=health_centers,
                schools=schools,
                famous_for=famous_for
            )
            created += 1

        self.stdout.write(self.style.SUCCESS(f"✅ Successfully seeded {created} RegionInfo records!"))
