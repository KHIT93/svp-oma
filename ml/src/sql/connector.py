import psycopg2
import psycopg2.extras

class Connector(object):
	"""docstring for Connector"""
	def __init__(self):
		self.DATABASE = 'svp-oma'
		self.USERNAME = 'postgres'
		self.PASSWORD = 'postgres'
		self.HOST = '10.135.17.153'
		self.PORT = '5432'

		self.conn = psycopg2.connect("dbname=%s user=%s password=%s host=%s port=%s" % (self.DATABASE, self.USERNAME, self.PASSWORD, self.HOST, self.PORT))
		self.cursor = self.conn.cursor(cursor_factory = psycopg2.extras.DictCursor)

	def execute(self, sqlstatement, sqldata = None):
		if sqldata is None:
			self.cursor.execute(sqlstatement)
			self.conn.commit()
		else:
			self.cursor.execute(sqlstatement, sqldata)
			self.conn.commit()

		return self.cursor.fetchall()

