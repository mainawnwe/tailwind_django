from django.db import models

# Create your models here.
from django.db import models


class YourModel(models.Model):
    # Define fields for your model here
    name = models.CharField(max_length=100)
    description = models.TextField()
