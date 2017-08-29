import error_code

class ErrorCodeRepo(object):
	"""docstring for ErrorCodeRepo"""
	def __init__(self):
		self.error_codes = {}

		self.DATABASE = 'svp-oma'
		self.USERNAME = 'postgres'
		self.PASSWORD = 'postgres'

		self.conn = psycopg2.connect("dbname=%s user=%s password=%s" % (self.DATABASE, self.USERNAME, self.PASSWORD))
		self.cursor = conn.cursor(cursor_factory = psycopg2.extras.DictCursor)

	def get(self, id):
		return self.error_codes[id]
		
	def getAll(self):
		sqlstatement = ("SELECT * FROM errors_errorcode")
		self.cursor.execute(sqlstatement)
		self.error_codes = self.cursor.fetchall()
		return self.error_codes