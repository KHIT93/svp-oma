from django.db import models

class WindturbineSetting(models.Model):
    windturbine_id = models.IntegerField(default=0)
    state = models.IntegerField()
    max_rpm_generator = models.IntegerField()
    max_temp_gearbox = models.DecimalField(max_digits=10, decimal_places=2)
    max_temp_generator = models.DecimalField(max_digits=10, decimal_places=2)
