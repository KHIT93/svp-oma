import base_model

class WindturbineError():
	"""
    The WindTurbineError class defines the logging format for errors registered at windturbines

    Each entry includes these fields:

    :param id: Unique identifier of this specific error/incident

    :param windturbine_id: Relationship to the windturbine that registered the error.

    :param timestamp: Timestamp in ISO8601 for when the error was registered at the windturbine

    :param error_message: The error message attached to the error code. This will normally be a copy of the message in the error_codes table, but is kept as a TextField to allow overriding it from Machine Learning

    :param error_code: The error code from the error_codes table

    :param resolved: Indicates if this incident has been resolved. The audit log will contain information about who/what solved the incident
    """
	def __init__(self, windturbine_id, timestamp, error_message, error_code, resolved):
        self.windturbine_id = windturbine_id
        self.timestamp = timestamp
        self.error_message = error_message
        self.error_code = error_codes
        self.resolved = resolved
		
