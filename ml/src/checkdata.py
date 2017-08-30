from repository.audit_log_repository import AuditLogRepo
from repository.error_code_repository import ErrorCodeRepo
from repository.windturbine_data_repository import WindturbineDataRepo
from repository.windturbine_error_repository import WindturbineErrorRepo
import pickle
from sklearn import tree
import numpy as np

auditLogRepo = AuditLogRepo()
errorCodeRepo = ErrorCodeRepo()
windturbineDataRepo = WindturbineDataRepo()
windturbineErrorRepo = WindturbineErrorRepo()

pickle_file = 'dtc_windturbine.pkl'
model_pkl = open(pickle_file, 'rb')
model = pickle.load(model_pkl)
model_pkl.close()

windturbineDataRepo.getNew()
order = [5, 3, 6, 9, 8, 0, 1, 2, 4, 7]
i = np.argsort(order)
type(windturbineDataRepo.windturbine_data)
test = windturbineDataRepo.windturbine_data[:,i]
#test = test[:,5]
print(test)
print(model.predict(test))
