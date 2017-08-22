from django.db import models

class LastSync(models.Model):
    key = models.CharField(models.CharField(default=255))
    value = models.TextField()