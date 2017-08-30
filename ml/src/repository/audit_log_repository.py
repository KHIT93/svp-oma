import psycopg2
import psycopg2.extras

class AuditLogRepo(object):
	"""docstring for AuditLogRepo"""
	def __init__(self):
		self.audit_logs = {}

		self.DATABASE = 'svp-oma'
		self.USERNAME = 'postgres'
		self.PASSWORD = 'postgres'

		self.conn = psycopg2.connect("dbname=%s user=%s password=%s" % (self.DATABASE, self.USERNAME, self.PASSWORD))
		self.cursor = conn.cursor(cursor_factory = psycopg2.extras.DictCursor)

	def save(self, audit_log):
		sqlstatement = ("INSERT INTO audit_log (timestamp, name, message, api_response, user_id) VALUES (%s, %s, %s, %s, %s) RETURNING id")
		sqldata = (audit_log.timestamp, audit_log.name, audit_log.message, audit_log.api_response, audit_log.user_id)
		self.cursor.execute(sqlstatement, sqldata)
		audit_log.id = cursor.fetchone()[0]
		self.audit_logs[audit_log.id] = audit_log
		return audit_log
