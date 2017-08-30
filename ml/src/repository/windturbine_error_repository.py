import time
import psycopg2
import psycopg2.extras

class WindturbineErrorRepo(object):
	"""docstring for ErrorCodeRepo"""
	def __init__(self):
		self.windturbine_errors = {}

		self.DATABASE = 'svp-oma'
		self.USERNAME = 'postgres'
		self.PASSWORD = 'postgres'
		self.HOST = '10.135.17.153'
		self.PORT = '5432'

		self.conn = psycopg2.connect("dbname=%s user=%s password=%s host=%s port=%s" % (self.DATABASE, self.USERNAME, self.PASSWORD, self.HOST, self.PORT))
		self.cursor = self.conn.cursor(cursor_factory = psycopg2.extras.DictCursor)

	def get(self, id):
		return self.windturbine_errors[id]

	def save(self, windturbine_error):
		sqlstatement = ("INSERT INTO windturbine_error (timestamp, error_message, error_code, windturbine_id, resolved) VALUES (%s, %s, %s, %s, %s) RETURNING id")
		sqldata = (windturbine_error.timestamp, windturbine_error.message, windturbine_error.code, windturbine_error.windturbine_id, False)
		self.cursor.execute(sqlstatement, sqldata)
		windturbine_error.id = cursor.fetchone()[0]
		self.windturbine_errors[windturbine_error.id] = windturbine_error
		return windturbine_error

	def dispose(self):
		self.cursor.close()
		self.conn.close()