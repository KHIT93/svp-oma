from django.db import models

class WindturbineSetting(models.Model):
    windturbine = models.IntegerField(default=0)
    state = models.IntegerField()
    brake = models.BooleanField(default=0)
    wind_speed = models.DecimalField(max_digits=10, decimal_places=2)
    wing_angle = models.DecimalField(max_digits=10, decimal_places=2)
    max_rpm_generator = models.IntegerField()
    max_temp_gearbox = models.DecimalField(max_digits=10, decimal_places=2)
    max_temp_generator = models.DecimalField(max_digits=10, decimal_places=2)
