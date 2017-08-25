import Motor
import time
import IRSensor
import RPi.GPIO as GPIO
import socket
import ADC
import pymysql.cursors


class Windturbine():
	"""docstring for Windturbine"""
	def __init__(self, motor, state, brake, wind_speed, wing_angle):
		self.motor = motor
		self.state = state
		self.brake = brake
		self.wind_speed = wind_speed
		self.wing_angle = wing_angle

	def changesettings(self):
		Motor.changespeed(self.wind_speed, self.wing_angle)
		
		if self.brake:
			self.motor.brake()

		if self.state == 0:
			self.motor.stop()
		elif self.state == 1:
			self.motor.run()

		
GPIO.cleanup()

# ADC channel, clock_pin, miso_pin, mosi_pin, cs_pin
adc = ADC.ADC(0, 23, 21, 19, 24)
# IR sensor pin
ir_sensor = IRSensor.IRSensor(7)
# PWM pin, Standby pin, AIN1 pin, PWM Frequincy, Duty
motor = Motor.Motor(3,5,11,1000, 0)
# Motor, state, brake, wind_speed, wing_angle
windturbine = Windturbine(motor, 0, 0, 0.0, 0.0)

# Database connection
cnx = pymysql.connect(user='root', password='P@ssw0rd', host='127.0.0.1', database='control_db')
cursor = cnx.cursor(pymysql.cursors.DictCursor)

# Windturbine data insertion statement
add_data = ("INSERT INTO windturbine_data_windturbinedata (windturbine, timestamp, state, temp_gearbox, temp_generator, rpm_generator, wind_speed) VALUES (%s, %s, %s, %s, %s, %s, %s)")
# Windturbine settings select statement
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
		# If there is a new config
		if cursor.execute(get_settings, current_config) > 0:
			row = cursor.fetchone()
			windturbine.state = row['state']
			windturbine.brake = row['brake']
			windturbine.wind_speed = row['wind_speed']
			windturbine.wing_angle = row['wing_angle']
			current_config = row['id']
			print(row['id'])
			windturbine.changesettings()
			



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
