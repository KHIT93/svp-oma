import base_model

class ErrorCode():
    """
    The ErrorCode class defines the format used for error codes and their severity
    Each entry includes these fields:

    :param id: Unique identifier for the error code

    :param code: A unique user defined numeric code

    :param message: A message that can be displayed in logs and UI notifications

    :param severity: A numeric value that defines the severity / priority of the error

    """
    def __init__(self, code, message, severity):
        self.code = code
        self.message = message
        self.severity = severity

        