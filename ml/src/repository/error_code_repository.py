import psycopg2
import psycopg2.extras

class ErrorCodeRepo(object):
	"""
	The ErrorCodeRepo class is a repository with connection to the errors_errorcode table
	"""
	def __init__(self):
		self.error_codes = {}

		self.DATABASE = 'svp-oma'
		self.USERNAME = 'postgres'
		self.PASSWORD = 'postgres'
		self.HOST = '10.135.17.153'
		self.PORT = '5432'

		self.conn = psycopg2.connect("dbname=%s user=%s password=%s host=%s port=%s" % (self.DATABASE, self.USERNAME, self.PASSWORD, self.HOST, self.PORT))
		self.cursor = self.conn.cursor(cursor_factory = psycopg2.extras.DictCursor)

	def get(self, code):
		if not self.error_codes:
			self.getAll()
		return list(filter(lambda x:x[2]==code,self.error_codes))
		
	def getAll(self):
		sqlstatement = ("SELECT * FROM errors_errorcode")
		self.cursor.execute(sqlstatement)
		self.error_codes = self.cursor.fetchall()
		return self.error_codes