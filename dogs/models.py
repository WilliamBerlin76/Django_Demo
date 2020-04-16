from django.db import models
from uuid import uuid4

class Dog(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=200)
    breed = models.CharField(max_length=200)
    weight = models.IntegerField()
