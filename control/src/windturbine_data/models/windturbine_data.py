from django.db import models

class WindturbineData(models.Model):
    windturbine = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
    state = models.IntegerField()
    temp_gearbox = models.DecimalField(max_digits=10, decimal_places=2)
    temp_generator = models.DecimalField(max_digits=10, decimal_places=2)
    rpm_generator = models.IntegerField()
    wind_speed = models.DecimalField(max_digits=10, decimal_places=2)
    wing_angle = models.DecimalField(max_digits=10, decimal_places=2)
    brake = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Windturbine data"