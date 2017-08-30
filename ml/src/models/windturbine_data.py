import base_model

class WindTurbineData():
	"""
    The WindTurbineData class defines the format in which we store the sensor information that has been recieved from the windturbines.

    Each entry includes these fields:

    :param windturbine_id: Relationship to the windturbine that collected the sensor data.

    :param timestamp: Timestamp in ISO 8601 for when the data was registered at the windturbine

    :param state: A numeric representation for the windturbine state at the time of this sensor reading

    :param temp_gearbox: Temperature reading in degrees Celcius from the gearbox

    :param temp_generator: Temperature reading in degrees Celcius from the generator

    :param rpm_generator: Reading of the current RPM registered at the generator

    :param wind_speed: Current reading of the wind speed at the windturbine
	"""
	def __init__(self, windturbine_id, timestamp, state, temp_gearbox, temp_generator, rpm_generator, wind_speed):
        self.windturbine_id = windturbine_id
    	self.timestamp = timestamp
    	self.state = state
    	self.temp_gearbox = temp_gearbox
    	self.temp_generator = temp_generator
    	self.rpm_generator = rpm_generator
    	self.wind_speed = wind_speed
    	
		