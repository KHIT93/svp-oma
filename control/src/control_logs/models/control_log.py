from django.db import models

class ControlLog(models.Model):
    """
    The ControlLog class is responsible for logs about a specific WindTurbine.

    Each entry holds the following information:

    :param id: Unique identifier for the logs of the WindTurbine

    :param timestamp: Timestamp for the entry in the log

    :param sensor_type_data: Which kind of sensor, there is logged

    :param current_value: The current value for the specific sensor

    :param windmill_state: The state the WindTurbine was in
    """
    timestamp = models.DateTimeField(auto_now_add=True)
    sensor_type_data = models.CharField(max_length=255)
    current_value = models.CharField(max_length=255)
    windmill_state = models.IntegerField()