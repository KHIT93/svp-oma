import base_model

class AuditLog():
	"""
	The AuditLog class defines the model used for logging actions and events happening in the application.
	This can fx. be when a user performs an action or when the system synchronizes data with the
	windturbines.

	Each entry has the following values:

	:param timestamp: Timestamp stored in ISO-8601

	:param user: Reference to the application user that caused the entry to be created.

	:param name: The name of the user or system component that caused the entry to be created.

	:param message: A message describing the performed action

	:param api_response: If an API call was performed this contains the API response that was recieved by the server
	"""
	def __init__(self, timestamp, user, name, message, api_response):
		self.timestamp = timestamp
		self.user = user
		self.name = name
		self.message = message
		self.api_response = api_response
		
