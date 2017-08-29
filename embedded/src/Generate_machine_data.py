import mysql.connector
import numpy as np


cnx = mysql.connector.connect(user='root', password='P@ssw0rd',
                              host='127.0.0.1',
                              database='SensorData')
cursor = cnx.cursor()

DROPTABLE = ("DROP TABLE test")

cursor.execute(DROPTABLE)
cnx.commit()

TABLE = ("CREATE TABLE `test` (`id` int(10) NOT NULL AUTO_INCREMENT,`rpm` int(5) NOT NULL,`temp` float(4) NOT NULL,`wind_speed` float(2) NOT NULL,`wing_angle` float(2) NOT NULL,`brake` int(1) NOT NULL,`error_code` int(4) NOT NULL,PRIMARY KEY (`id`)) ENGINE=InnoDB")

cursor.execute(TABLE)
cnx.commit()

add_data = ("INSERT INTO test "
			"(rpm, temp, wind_speed, wing_angle, brake, error_code) "
			"VALUES (%s, %s, %s, %s, %s, %s)")

for x in range(1,10000):
	temp = np.random.uniform(15.0, 29)
	rpm = np.random.randint(1000, 2000)
	wing_angle = np.random.uniform(0.0,10.0)
	wind_speed = np.random.uniform((rpm / 80) + wing_angle, (rpm / 80) + wing_angle + 5)
	brake = 0

	error_code = 0

	data_data = (rpm, round(temp, 4), round(wind_speed, 1), round(wing_angle,1), brake, error_code)

	cursor.execute(add_data, data_data)

for x in range(1,10000):
	temp = 0
	rpm = np.random.randint(1000, 2500)
	wing_angle = np.random.uniform(0.0,10.0)
	wind_speed = np.random.uniform((rpm / 80) + wing_angle, (rpm / 80) + wing_angle + 5)
	brake = 0

	error_code = 100

	data_data = (rpm, round(temp, 4), round(wind_speed, 1), round(wing_angle,1), brake, error_code)

	cursor.execute(add_data, data_data)

for x in range(1,10000):
	temp = np.random.uniform(30.0, 40.0)
	rpm = np.random.randint(2050, 2500)
	wing_angle = np.random.uniform(0.0,10.0)
	wind_speed = np.random.uniform((rpm / 80) + wing_angle, (rpm / 80) + wing_angle + 5)
	brake = 0

	error_code = 110

	data_data = (rpm, round(temp, 4), round(wind_speed, 1), round(wing_angle,1), brake, error_code)

	cursor.execute(add_data, data_data)

for x in range(1,10000):
	temp = np.random.uniform(30.0, 40.0)
	rpm = np.random.randint(800, 1500)
	wing_angle = np.random.uniform(0.0,10.0)
	wind_speed = np.random.uniform((rpm / 80) + wing_angle, (rpm / 80) + wing_angle + 5)
	brake = 0

	error_code = 120

	data_data = (rpm, round(temp, 4), round(wind_speed, 1), round(wing_angle,1), brake, error_code)

	cursor.execute(add_data, data_data)

for x in range(1,10000):
	temp = np.random.uniform(30.0, 40.0)
	rpm = 0
	wing_angle = np.random.uniform(0.0,10.0)
	wind_speed = 0
	brake = 0

	error_code = 130

	data_data = (rpm, round(temp, 4), round(wind_speed, 1), round(wing_angle,1), brake, error_code)

	cursor.execute(add_data, data_data)

for x in range(1,10000):
	temp = np.random.uniform(15.0, 29)
	rpm = 0
	wing_angle = np.random.uniform(0.0,10.0)
	wind_speed = np.random.uniform(0 + wing_angle, 20 + wing_angle + 5)
	brake = 0

	error_code = 200

	data_data = (rpm, round(temp, 4), round(wind_speed, 1), round(wing_angle,1), brake, error_code)

	cursor.execute(add_data, data_data)

for x in range(1,10000):
	temp = np.random.uniform(15.0, 29)
	rpm = np.random.randint(2050, 2500)
	wing_angle = np.random.uniform(0.0,10.0)
	wind_speed = np.random.uniform((rpm / 80) + wing_angle, (rpm / 80) + wing_angle + 5)
	brake = 0

	error_code = 210

	data_data = (rpm, round(temp, 4), round(wind_speed, 1), round(wing_angle,1), brake, error_code)

	cursor.execute(add_data, data_data)

for x in range(1,10000):
	temp = np.random.uniform(15.0, 29)
	rpm = np.random.randint(0, 1200)
	wing_angle = np.random.uniform(2.0,10.0)
	wind_speed = np.random.uniform((rpm / 80) + wing_angle, (rpm / 80) + wing_angle + 5)
	brake = 0

	error_code = 220

	data_data = (rpm, round(temp, 4), round(wind_speed, 1), round(wing_angle,1), brake, error_code)

	cursor.execute(add_data, data_data)

for x in range(1,10000):
	temp = np.random.uniform(30.0, 40.0)
	rpm = np.random.randint(2050, 2500)
	wind_speed = np.random.uniform(rpm / 70, (rpm / 70 + 5))
	wing_angle = 10
	brake = 1

	error_code = 300

	data_data = (rpm, round(temp, 4), round(wind_speed, 1), round(wing_angle,1), brake, error_code)


cursor.execute(add_data, data_data)
cnx.commit()



cursor.close()
cnx.close()