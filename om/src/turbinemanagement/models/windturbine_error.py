from django.db import models
from appcore.models.base_model import BaseModel
from .windturbine import WindTurbine

# === Model used to get errors from windturbines ===

class WindTurbineError(BaseModel):
    """
    The WindTurbineError class defines the logging format for errors registered at windturbines

    Each entry includes these fields:

    :param id: Unique identifier of this specific error/incident

    :param windturbine: Relationship to the windturbine that registered the error. In the SQL database, this reference is stored as windturbine_id

    :param timestamp: Timestamp in ISO8601 for when the error was registered at the windturbine

    :param error_message: The error message attached to the error code. This will normally be a copy of the message in the error_codes table, but is kept as a TextField to allow overriding it from Machine Learning

    :param error_code: The error code from the error_codes table

    :param resolved: Indicates if this incident has been resolved. The audit log will contain information about who/what solved the incident
    """
    windturbine = models.ForeignKey(WindTurbine)
    timestamp = models.DateTimeField(auto_now_add=True)
    error_message = models.TextField()
    error_code = models.IntegerField()
    resolved = models.BooleanField(default=False)

    def __str__(self):
        return str(self.windturbine)
