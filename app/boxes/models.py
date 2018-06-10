from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Boxes(models.Model):
    type = models.CharField(max_length=100, default="cuboid", blank=False)
    created_by = models.ForeignKey(User, related_name="user", on_delete=models.CASCADE)
    length = models.FloatField(blank=False)
    breadth = models.FloatField(blank=False)
    height = models.FloatField(blank=False)


