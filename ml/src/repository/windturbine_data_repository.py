import psycopg2
import psycopg2.extras
import numpy as np

class WindturbineDataRepo(object):
	"""
	The WindturbineDataRepo class is a repository with connection to the turbinemanagement_windturbinedata table
	:type name: Connector
	:param name: A initialized connector object
	"""
	def __init__(self, connector):
		self.windturbine_data = []
		self.last_record = 0
		self.connector = connector

	def get(self, id):
		return self.windturbine_data[id]

	def get_new(self, windturbine_id):
		sqlstatement = ("SELECT * FROM turbinemanagement_windturbinedata WHERE id > %s AND windturbine_id = %s ORDER BY id")
		sql_data = ([self.last_record], windturbine_id)
		self.windturbine_data = self.connector.execute(sqlstatement, sql_data)
		self.last_record = self.windturbine_data[-1]
		self.windturbine_data = np.average(self.windturbine_data)
		print(self.windturbine_data)
