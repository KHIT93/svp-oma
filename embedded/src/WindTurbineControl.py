import Motor
import time
import IRSensor
import RPi.GPIO as GPIO
import socket
import ADC
import pymysql.cursors


cnx = pymysql.connect(user='root', password='P@ssw0rd',
                              host='127.0.0.1',
                              database='control_db')
cursor = cnx.cursor()
add_data = ("INSERT INTO windturbine_data_windturbinedata "
			"(windturbine, timestamp, state, temp_gearbox, temp_generator, rpm_generator, wind_speed) "
			"VALUES (%s, %s, %s, %s, %s, %s, %s)")

GPIO.cleanup()

# ADC channel, clock_pin, miso_pin, mosi_pin, cs_pin
adc = ADC.ADC(0, 23, 21, 19, 24)
# IR sensor pin
ir_sensor = IRSensor.IRSensor(7)
# PWM pin, Standby pin, AIN1 pin, PWM Frequincy, Duty
motor = Motor.Motor(3,5,11,1000,25.0)
temperature = 0
Motor.run(motor)
rpm = 0.0
while temperature < 30:
	value = ADC.readadc(adc)
	volts = (value * 3.3) / 1024
	temperature = volts / (10.0 / 1000)
	rpm = IRSensor.read_rpm()
	print(temperature)
	data_data = (1, time.localtime(), 1, temperature, temperature, rpm, 20.0)
	cursor.execute(add_data, data_data)
	cnx.commit()
	time.sleep(0.25)

cursor.close()
cnx.close()
 