from django.db import models
from uuid import uuid4

class Dog(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=200)
    description = models.CharField(blank=True, max_length=1000)
    breed = models.CharField(max_length=200)
    weight = models.IntegerField()
    friendly = models.BooleanField(default=True)