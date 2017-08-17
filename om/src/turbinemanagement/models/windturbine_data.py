from django.db import models
from appcore.models.base_model import BaseModel
from .windturbine import WindTurbine

class WindTurbineData(BaseModel):
    windturbine = models.ForeignKey(WindTurbine)
    timestamp = models.DateTimeField(auto_now_add=True)
    state = models.IntegerField()
    temp_gearbox = models.DecimalField(max_digits=10, decimal_places=2)
    temp_generator = models.DecimalField(max_digits=10, decimal_places=2)
    rpm_generator = models.IntegerField()
    wind_speed = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.windturbine)
