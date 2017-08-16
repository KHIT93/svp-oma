from django.db import models

class WindturbineSetting(models.Model):
    windturbine_id = models.IntegerField(default=0)
    state = models.CharField(max_length=255)
    max_rpm_generator = models.IntegerField(default=0)
    max_temp_gearbox = models.IntegerField(default=0)
    max_temp_generator = models.IntegerField(default=0)
