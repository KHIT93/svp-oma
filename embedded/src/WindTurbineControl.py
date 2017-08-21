import Motor
import time
import IRSensor
import RPi.GPIO as GPIO
import socket
import ADC
import mysql.connector


cnx = mysql.connector.connect(user='root', password='P@ssw0rd',
                              host='127.0.0.1',
                              database='SensorData')
cursor = cnx.cursor()
#TABLE = ("CREATE TABLE `data` (`id` int(10) NOT NULL AUTO_INCREMENT,`rpm` int(5) NOT NULL,`temp` float(4) NOT NULL,PRIMARY KEY (`id`)) ENGINE=InnoDB")
add_data = ("INSERT INTO data "
			"(rpm, temp) "
			"VALUES (%s, %s)")

#cursor.execute(TABLE)
#cursor.close()
#cnx.close()



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
while temperature < 28:
	value = ADC.readadc(adc)
	volts = (value * 3.3) / 1024
	temperature = volts / (10.0 / 1000)
	print(temperature)
	rpm = IRSensor.read_rpm()
	print(rpm)

	data_data = (rpm, temperature)
	cursor.execute(add_data, data_data)
	time.sleep(0.5)
cnx.commit()
cursor.close()
cnx.close()
'''
while rpm < 2000:
	rpm = IRSensor.read_rpm()
	time.sleep(1)
	print(rpm)
	Motor.changespeed(motor, motor.duty+0.1)


TCP_IP = '0.0.0.0'
TCP_PORT = 5005
BUFFER_SIZE = 1024  # Normally 1024, but we want fast response

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

while True:
	print("waiting..")
	conn, addr = s.accept()
	print('Connection address:', addr)
	data = conn.recv(BUFFER_SIZE)
	if data: 
		print("received data:", data)
		Motor.changespeed(motor, float(data))
	conn.close()
'''


# The channel from where we want to read on the ADC chip

 

	