import Motor
import time
import IRSensor
import RPi.GPIO as GPIO
import socket
import ADC
import pymysql.cursors

# Config data: windturbine, State, Brake, Wind_speed, Wing_angle
# Out data: windturbine, timestamp, state, temp_gearbox, temp_generator, rpm_generator, wind_speed, wing_angle, brake

GPIO.cleanup()

# State of the windturbine 1 = running, 0 = stopped
state = 1
# State on the brake 1 = Activated, 0 = deactivated
brake = 0
# Speed of wind in meters/second
wind_speed = 20
# Angle of the wind turbine wings in degress (Max = 10)
wing_angle = 0

# ADC channel, clock_pin, miso_pin, mosi_pin, cs_pin
adc = ADC.ADC(0, 23, 21, 19, 24)
# IR sensor pin
ir_sensor = IRSensor.IRSensor(7)
# PWM pin, Standby pin, AIN1 pin, PWM Frequincy, Duty
motor = Motor.Motor(3,5,11,1000,0)
# Start the motor
Motor.run(motor)


# Database connection
cnx = pymysql.connect(user='root', password='P@ssw0rd',
                              host='127.0.0.1',
                              database='control_db')
cursor = cnx.cursor(pymysql.cursors.DictCursor)
# Windturbine data insertion string
add_data = ("INSERT INTO windturbine_data_windturbinedata "
			"(windturbine, timestamp, state, temp_gearbox, temp_generator, rpm_generator, wind_speed) "
			"VALUES (%s, %s, %s, %s, %s, %s, %s)")

get_settings = ("SELECT * FROM windturbine_settings_windturbinesetting WHERE id > %s ORDER BY id desc")

# Variables initialized for later
temperature = 0
rpm = 0.0
get_config_count = 8
current_config = 0

while True:
	# Check for new config
	if get_config_count > 4:
		get_config_count = 0
		Motor.changespeed(motor, wind_speed, wing_angle)
		cursor.execute(get_settings, current_config)
		if cursor.fetchone():
			state = cursor['state']
			brake = cursor['brake']
			wind_speed = cursor['wind_speed']
			wing_angle = cursor['wing_angle']
			current_config = cursor['id']
			print(cursor['id'])

	# Read ADC
	value = ADC.readadc(adc)
	# Take the reading and multiply it by the volts on the ADC. Then divide by the amount of bits from the ADC
	volts = (value * 3.3) / 1024
	temperature = volts / (10.0 / 1000)
	# Read RPM
	rpm = IRSensor.read_rpm()

	# Prepare the insertion data, then insert into database and commit
	data_data = (1, time.localtime(), 1, temperature, temperature, rpm, 20.0)
	cursor.execute(add_data, data_data)
	cnx.commit()

	get_config_count += 1
	time.sleep(1)

cursor.close()
cnx.close()
