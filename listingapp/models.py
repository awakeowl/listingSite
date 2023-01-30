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
