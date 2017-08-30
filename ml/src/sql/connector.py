

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

	def execute(sqlstatement):
		self.cursor.execute(sqlstatement)
		self.conn.commit()

		return self.cursor.fetchall()

	def execute(sqlstatement, sqldata):
		self.cursor.execute(sqlstatement, sqldata)
		self.conn.commit()

		return self.cursor.fetchall()

