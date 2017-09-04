class WindturbineRepo(object):
	"""
	The WindturbineDataRepo class is a repository with connection to the turbinemanagement_windturbinedata table
	:type name: Connector
	:param name: A initialized connector object
	"""
	def __init__(self, connector):
		self.windturbine = []
		self.connector = connector

	def get(self, id):
		return self.windturbine[id]

	def get_turbines(self):
		sqlstatement = ("SELECT * FROM turbinemanagement_windturbine")
		self.windturbine = self.connector.execute(sqlstatement)
