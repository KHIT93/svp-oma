import psycopg2
import psycopg2.extras

class AuditLogRepo(object):
	"""
	The AuditLogRepo class is a repository with connection to the audit_log table
	"""
	def __init__(self):
		self.audit_logs = {}

		self.DATABASE = 'svp-oma'
		self.USERNAME = 'postgres'
		self.PASSWORD = 'postgres'
		self.HOST = '10.135.17.153'
		self.PORT = '5432'

		self.conn = psycopg2.connect("dbname=%s user=%s password=%s host=%s port=%s" % (self.DATABASE, self.USERNAME, self.PASSWORD, self.HOST, self.PORT))
		self.cursor = self.conn.cursor(cursor_factory = psycopg2.extras.DictCursor)

	def save(self, audit_log):
		sqlstatement = ("INSERT INTO audit_log (timestamp, name, message, api_response, user_id) VALUES (%s, %s, %s, %s, %s) RETURNING id")
		sqldata = (audit_log.timestamp, audit_log.name, audit_log.message, audit_log.api_response, audit_log.user_id)
		self.cursor.execute(sqlstatement, sqldata)
		audit_log.id = cursor.fetchone()[0]
		self.audit_logs[audit_log.id] = audit_log
		return audit_log
