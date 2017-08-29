from django.db import models

class WindturbineSetting(models.Model):
    """
    The WindturbineSetting class is responsible for holding the settings related to a specific WindTurbine

    Each entry holds the following information:

    :param id: Unique identifier for the settings of the WindTurbine

    :param windturbine: Relationship to the WindTurbine using these settings. In the SQL database, this reference is saved as windturbine_id

    :param state: The normal state for of operation the this WindTurbine

    :param brake: Defines if the brake are active

    :param wing_angle: Defines the angle of the wing

    :param max_rpm_generator: The maximum threshold for the rpm at the generator

    :param max_temp_gearbox: The maximum threshold for the temp of the gearbox

    :param max_temp_generator: The maximum threshold for the temp at the generator

    """
    windturbine = models.IntegerField(default=0)
    state = models.IntegerField()
    brake = models.BooleanField(default=False)
    wing_angle = models.DecimalField(max_digits=10, decimal_places=2)
    max_rpm_generator = models.IntegerField()
    max_temp_gearbox = models.DecimalField(max_digits=10, decimal_places=2)
    max_temp_generator = models.DecimalField(max_digits=10, decimal_places=2)
