from repository.audit_log_repository import AuditLogRepo
from repository.error_code_repository import ErrorCodeRepo
from repository.windturbine_data_repository import WindturbineDataRepo
from repository.windturbine_error_repository import WindturbineErrorRepo
from models.windturbine_error import WindturbineError
import pickle
from sklearn import tree
import time
import numpy as np

# init repositories
auditLogRepo = AuditLogRepo()
errorCodeRepo = ErrorCodeRepo()
windturbineDataRepo = WindturbineDataRepo()
windturbineErrorRepo = WindturbineErrorRepo()

# get the saved model
pickle_file = 'dtc_windturbine.pkl'
model_pkl = open(pickle_file, 'rb')
model = pickle.load(model_pkl)
model_pkl.close()

# Get new data
windturbineDataRepo.getNew()
# The order of the data for the machinelearning
order = [5, 3, 6, 9, 8]
# Convert from list to array
dataarray = np.array(windturbineDataRepo.windturbine_data)
# Create array with the correct order
machinelearningarray = dataarray[:,order]
# Run prediction and save into an array
prediction = model.predict(machinelearningarray)
i = 0
for x in prediction:
	print(x)
	if x not 0:
		error = np.array(errorCodeRepo.get(x))
		windturbine_error = WindturbineError(dataarray[i,7], dataarray[i,1], error[0,1], x, False)
		windturbineErrorRepo.save(windturbine_error)

	i += 1