from django.db import models

# RegionInfo model for storing state, district, taluk, and region-related information
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


# Hospital model to store information about hospitals in each taluk
class Hospital(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    region = models.ForeignKey(RegionInfo, related_name='hospitals_in_region', on_delete=models.CASCADE)  # ForeignKey to RegionInfo

    def __str__(self):
        return f"{self.name} - {self.region.taluk}"  # Access taluk via the related RegionInfo model


# School model to store information about schools in each taluk
class School(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    region = models.ForeignKey(RegionInfo, related_name='schools_in_region', on_delete=models.CASCADE)  # ForeignKey to RegionInfo

    def __str__(self):
        return f"{self.name} - {self.region.taluk}"  # Access taluk via the related RegionInfo model
