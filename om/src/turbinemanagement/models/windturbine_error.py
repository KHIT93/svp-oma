from django.db import models
from appcore.models.base_model import BaseModel
from .windturbine import WindTurbine

class WindTurbineError(BaseModel):
    windturbine = models.ForeignKey(WindTurbine)
    timestamp = models.DateTimeField(auto_now_add=True)
    error_messge = models.TextField()
    error_code = models.IntegerField()
    resolved = models.BooleanField(default=False)

    def __str__(self):
        return str(self.windturbine)
