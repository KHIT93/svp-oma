import psycopg2
import psycopg2.extras

class ErrorCodeRepo(object):
	"""
	The ErrorCodeRepo class is a repository with connection to the errors_errorcode table
	:type name: Connector
	:param name: A initialized connector object
	"""
	def __init__(self, connector):
		self.error_codes = {}
		self.connector = connector

	def get(self, code):
		if not self.error_codes:
			self.getAll()
		return list(filter(lambda x:x[2]==code,self.error_codes))
		
	def getAll(self):
		sqlstatement = ("SELECT * FROM errors_errorcode")
		self.error_codes = self.connector.execute(sqlstatement)
		return self.error_codes