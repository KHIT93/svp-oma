from django.db import models

class WindturbineData(models.Model):
    """
    The WindTurbineData class defines the format in which we store the sensor information that has been recieved from the windturbines.

    Each entry includes these fields:

    :param id: Unique identifier for the specific sensor reading

    :param windturbine: Relationship to the windturbine that collected the sensor data. In the SQL database, this reference is stored as windturbine_id

    :param timestamp: Timestamp in ISO 8601 for when the data was registered at the windturbine

    :param state: A numeric representation for the windturbine state at the time of this sensor reading

    :param temp_gearbox: Temperature reading in degrees Celcius from the gearbox

    :param temp_generator: Temperature reading in degrees Celcius from the generator

    :param rpm_generator: Reading of the current RPM registered at the generator

    :param wind_speed: Current reading of the wind speed at the windturbine

    :param wing_angle: The angle of the turbine wings

    :param brake: Defines if the brakes are active
    """
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