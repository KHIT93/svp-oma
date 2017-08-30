import psycopg2
import psycopg2.extras

class ErrorCodeRepo(object):
	"""docstring for ErrorCodeRepo"""
	def __init__(self):
		self.error_codes = {}

		self.DATABASE = 'svp-oma'
		self.USERNAME = 'postgres'
		self.PASSWORD = 'postgres'
		self.HOST = '10.135.17.153'
		self.PORT = '5432'

		self.conn = psycopg2.connect("dbname=%s user=%s password=%s host=%s port=%s" % (self.DATABASE, self.USERNAME, self.PASSWORD, self.HOST, self.PORT))
		self.cursor = self.conn.cursor(cursor_factory = psycopg2.extras.DictCursor)

	def get(self, id):
		return self.error_codes[id]
		
	def getAll(self):
		sqlstatement = ("SELECT * FROM errors_errorcode")
		self.cursor.execute(sqlstatement)
		self.error_codes = self.cursor.fetchall()
		return self.error_codes