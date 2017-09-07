import psycopg2
import psycopg2.extras

class AuditLogRepo(object):
	"""
	The AuditLogRepo class is a repository with connection to the audit_log table
	:type name: Connector
	:param name: A initialized connector object
	"""
	def __init__(self, connector):
		self.audit_logs = {}
		self.connector = connector

	def save(self, audit_log):
		sqlstatement = ("INSERT INTO audit_log (timestamp, name, message, api_response, user_id) VALUES (%s, %s, %s, %s, %s) RETURNING id")
		sqldata = (audit_log.timestamp, audit_log.name, audit_log.message, audit_log.api_response, audit_log.user_id)
		result = self.connector.execute(sqlstatement, sqldata)
		# Get id of the created log
		audit_log.id = np.array(result)[0,0]
		# save the log in the repository
		self.audit_logs[audit_log.id] = audit_log
		return audit_log
