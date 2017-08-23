from django.db import models
from appcore.models.base_model import BaseModel

class WindFarm(BaseModel):
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        if self.name == None or self.name == "":
            return str(self.id)
        else:
            return str(str(self.id) + " (" + self.name + ")")
