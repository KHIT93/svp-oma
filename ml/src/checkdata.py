from audit_log_repository import AuditLogRepo
from error_code_repository import ErrorCodeRepo
from windturbine_data_repository import WindturbineDataRepo
from windturbine_error_repository import WindturbineErrorRepo
import pickle
from sklearn import tree

auditLogRepo = AuditLogRepo()
errorCodeRepo = ErrorCodeRepo()
windturbineDataRepo = WindturbineDataRepo()
windturbineErrorRepo = WindturbineErrorRepo()

pickle_file = 'dtc_windturbine.pkl'
model_pkl = open(pickle_file, 'rb')
model = pickle.load(model_pkl)
model_pkl.close()

windturbineDataRepo.getNew()
print(windturbineDataRepo.windturbine_data)
