from django.db import models

class StateColor(models.Model):
    state_name = models.CharField(max_length=100, unique=True)  # e.g., 'Maharashtra'
    color_code = models.CharField(max_length=7)  # e.g., #FF0000

    def __str__(self):
        return f"{self.state_name}: {self.color_code}"

class RegionInfo(models.Model):
    state = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    taluk = models.CharField(max_length=100)
    population = models.IntegerField()
    literacy_rate = models.FloatField()
    health_centers = models.IntegerField()
    schools = models.IntegerField()
    famous_for = models.TextField()

    def __str__(self):
        return f"{self.state}, {self.district}, {self.taluk}"
    