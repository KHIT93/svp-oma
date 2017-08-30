from repository.audit_log_repository import AuditLogRepo
from repository.error_code_repository import ErrorCodeRepo
from repository.windturbine_data_repository import WindturbineDataRepo
from repository.windturbine_error_repository import WindturbineErrorRepo
from models.windturbine_error import WindturbineError
import pickle
from sklearn import tree
import time
import numpy as np
from sql.connector import Connector

conn = Connector()
# init repositories
audit_log_repo = AuditLogRepo()
error_code_repo = ErrorCodeRepo(conn)
windturbine_data_repo = WindturbineDataRepo()
windturbine_error_repo = WindturbineErrorRepo()

# get the saved model
pickle_file = 'dtc_windturbine.pkl'
model_pkl = open(pickle_file, 'rb')
model = pickle.load(model_pkl)
model_pkl.close()

while True:
	# Get new data
	windturbine_data_repo.getNew()
	# The order of the data for the machinelearning
	order = [5, 3, 6, 9, 8]
	# Convert from list to array
	data_array = np.array(windturbine_data_repo.windturbine_data)
	# Create array with the correct order
	machinelearning_array = data_array[:,order]
	# Run prediction and save into an array
	prediction = model.predict(machinelearning_array)
	i = 0
	for x in prediction:
		print(x)
		if x > 0:
			error = np.array(error_ode_epo.get(x))
			windturbine_error = WindturbineError(data_array[i,7], data_array[i,1], error[0,1], x, False)
			windturbine_error_repo.save(windturbine_error)
		
		i += 1