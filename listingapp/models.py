import uuid
from django.db import models


class Location(models.Model):
    id = models.UUIDField(
        primary_key=True, editable=False, default=uuid.uuid4())
    name = models.CharField(max_length=100)
    description = models.TextField()
    # image =

    def __str__(self) -> str:
        return self.name


class Project(models.Model):
    id = models.UUIDField(
        primary_key=True, editable=False, default=uuid.uuid4())
    name = models.CharField(max_length=100)
    amenities = models.ManyToManyField('Amenity', related_name='amenities')
    location = models.ForeignKey(
        Location, related_name='project', on_delete=models.CASCADE)
    description = models.TextField()
    developer = models.CharField(max_length=55, blank=True, null=True)
    units = models.IntegerField(blank=True, null=True)
    completion_date = models.DateField(blank=True, null=True)
    map_location = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self) -> str:
        return self.name
