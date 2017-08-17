from django.db import models

class WindturbineData(models.Model):
    windturbine_id = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    state = models.CharField(max_length=255)
    temp_gearbox = models.IntegerField(default=0)
    temp_generator = models.IntegerField(default=0)
    rpm_generator = models.IntegerField(default=0)
    wind_speed = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = "Windturbine data"