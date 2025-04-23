🌍 Geographic Data Visualization Web App

A full-stack web application built with Django 5.1.6 and Leaflet.js that allows users to explore administrative regions in India (states, districts, taluks) interactively. Users can click or select regions on the map to view detailed socio-economic and infrastructural data in a responsive side panel, complete with dynamic charts.

🚀 Features

Interactive Map: Built with Leaflet.js v1.9.4, supporting GeoJSON overlays for multi‑level boundaries.

Region Highlighting: Click or dropdown selection triggers real-time highlight and style update via Leaflet’s setStyle().

Data Panel: Displays region metadata (population, literacy_rate, health_centers, schools, famous_for) fetched from the Django backend.

Dynamic Charts: Chart.js v4.3.0 renders bar and line charts for key metrics on each selection.

Color Coding: Uses Chromajs v2.1.0 for choropleth color scales, driven by a StateColor Django model.

RESTful API: Django REST Framework endpoints serve filtered GeoJSON and region info.

Seed Command: manage.py faker populates the RegionInfo table from static/geojson/india_city.geojson.

Responsive Design: Bootstrap 5 grid layout ensures usability on desktop and mobile.

🧰 Technology Stack

Backend: Python 3.x, Django 5.1.6, Django REST Framework

Database: SQLite3 (dev), PostgreSQL + PostGIS (production)

Frontend:

HTML5, CSS3, JavaScript (ES6)

Bootstrap 5

Leaflet.js v1.9.4

Chart.js v4.3.0

Chromajs v2.1.0

Dev Tools: Git, VS Code, Postman, Docker (optional)

📂 Project Structure

map_plus/                  # Django project root
├── map_plus/              # Project settings
│   ├── settings.py        # Django 5.1.6 configuration
│   ├── urls.py            # Root URL includes `mapapp.urls`
│   └── wsgi.py / asgi.py
├── mapapp/                # Core application
│   ├── models.py          # `StateColor`, `RegionInfo`
│   ├── views.py           # index & API views
│   ├── urls.py            # API endpoint routes
│   ├── management/commands/faker.py  # Seed data command
│   └── templates/         # `waste1.html`
├── static/geojson/        # GeoJSON files
│   ├── india_states.geojson
│   ├── india_dist.geojson.json
│   └── india_city.geojson
├── db.sqlite3             # Development database
└── manage.py              # Django CLI

⚙️ Installation & Setup

Clone the repository

git clone https://github.com/Manu-1101/geographic-data-visualizer.git
cd geographic-data-visualizer

Create & activate a virtual environment

python -m venv venv
source venv/bin/activate    # Windows: venv\Scripts\activate

Install dependencies

pip install -r requirements.txt

Run migrations

python manage.py migrate

Seed the database

python manage.py faker

Start the server

python manage.py runserver

Open in browser

http://127.0.0.1:8000/

🔍 Usage

Use the level selector (State/District/City) to update map granularity.

Click on a region polygon to highlight and fetch data.

Results appear in the info panel on the right, with interactive charts.

🎨 Customization

Styling: Modify mapapp/templates/waste1.html CSS or swap Bootstrap theme.

Color Schemes: Update StateColor entries or adjust Chromajs scale parameters in leaflet-integration.js.

Data Models: Extend RegionInfo to include additional metrics or relationships.

🚀 Deployment

Suggested production setup:

Switch to PostgreSQL + PostGIS in settings.py.

Configure Allowed Hosts and SECRET_KEY via env variables.

Use Gunicorn + Nginx or deploy to Heroku/AWS Elastic Beanstalk.

Enable CI/CD with GitHub Actions or GitLab CI for automated tests.

🤝 Contributing

Contributions are welcome! Please follow these steps:

Fork the repository

Create a new branch: git checkout -b feature/my-feature

Commit your changes: `git commit -m "Add feature"

Push: git push origin feature/my-feature

Open a Pull Request for review.

📄 License

This project is licensed under the MIT License. See LICENSE for details.

👤 Author

Name: K Manoj Kumar
Role: Software Developer Intern @ Social Bytes
Aspiration: DevOps Engineer
Email: kamnojkumar161@gmail.com
GitHub: github.com/Manu-1011
LinkedIn: linkedin.com/in/k-manoj-kumar11/
