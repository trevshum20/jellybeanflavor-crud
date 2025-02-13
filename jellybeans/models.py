from django.db import models

# Create your models here.

class JellybeanFlavor(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.CharField(max_length=255, blank=True)
    photoUrl = models.CharField(max_length=255)

    def __str__(self):
        return self.name
