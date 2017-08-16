from django.db import models
from appcore.models.base_model import BaseModel
from .windfarm import WindFarm

class WindTurbine(BaseModel):
    name = models.CharField(max_length=100, null=True, blank=True)
    longtitude = models.FloatField()
    latitude = models.FloatField()
    windfarm = models.ForeignKey(WindFarm)

    def __str__(self):
        if name == None:
            return str(self.id)
        else:
            return str(self.name)
