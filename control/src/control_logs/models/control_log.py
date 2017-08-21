from django.db import models

class ControlLog(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    sensor_type_data = models.CharField(max_length=255)
    current_value = models.CharField(max_length=255)
    windmill_state = models.IntegerField()