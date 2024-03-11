from django.db import models
from django.utils import timezone

class Phone(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    price = models.FloatField()
    release_date = models.DateField(default=timezone.now)
    is_available = models.BooleanField(default=True)
    slug = models.SlugField(max_length=255)

    def __str__(self):
        return self.name