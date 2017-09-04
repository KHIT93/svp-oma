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
		sql_data = (self.last_record, windturbine_id)
		self.windturbine_data = self.connector.execute(sqlstatement, sql_data)
		if self.windturbine_data:
			self.last_record = self.windturbine_data[-1][0]
			first_datetime = self.windturbine_data[0][1]
			last_datetime = self.windturbine_data[-1][1]
			mean_datetime = first_datetime + (last_datetime - first_datetime) / 2
			order = [0, 2, 3, 4, 5, 6, 7, 8, 9]
			self.windturbine_data = np.average(np.array(self.windturbine_data)[:, order], axis=0)
			self.windturbine_data = np.insert(self.windturbine_data, 1, mean_datetime)
			print(self.windturbine_data)
		
