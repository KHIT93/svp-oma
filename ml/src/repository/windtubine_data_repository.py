import windturbine_data
import psycopg2
import psycopg2.extras

class WindturbineDataRepo(object):
	"""docstring for WindturbineDataRepo"""

	def __init__(self):
		self.windturbine_data = {}
		self.last_record = 0

		self.DATABASE = 'svp-oma'
		self.USERNAME = 'postgres'
		self.PASSWORD = 'postgres'

		self.conn = psycopg2.connect("dbname=%s user=%s password=%s" % (self.DATABASE, self.USERNAME, self.PASSWORD))
		self.cursor = conn.cursor(cursor_factory = psycopg2.extras.DictCursor)

	def get(self, id):
		return self.windturbine_data[id]

	def getNew(self):
		sqlstatement = ("SELECT * FROM turbinemanagement_windturbinedata WHERE id > %s ORDER BY id")
		self.cursor.execute(sqlstatement, last_record)
		self.windturbine_data = self.cursor.fetchall()

	def dispose(self):
		self.cursor.close()
		self.conn.close()
