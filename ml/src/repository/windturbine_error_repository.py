
from sql.connector import Connector

class WindturbineErrorRepo(object):
	"""
	The WindturbineErrorRepo class is a repository with connection to the turbinemanagement_windturbineerror table
	"""
	def __init__(self, connector):
		self.windturbine_errors = {}
		self.connector = connector

	def get(self, id):
		return self.windturbine_errors[id]

	def save(self, windturbine_error):
		sqlstatement = ("INSERT INTO turbinemanagement_windturbineerror (timestamp, error_message, error_code, windturbine_id, resolved) VALUES (%s, %s, %s, %s, %s) RETURNING id")
		sqldata = (windturbine_error.timestamp, windturbine_error.error_message, windturbine_error.error_code, windturbine_error.windturbine_id, False)
		windturbine_error.id = Connector.execute()[0]
		self.windturbine_errors[windturbine_error.id] = windturbine_error
		return windturbine_error

	def dispose(self):
		self.cursor.close()
		self.conn.close()