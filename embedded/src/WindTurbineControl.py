import Motor
import time
import IRSensor
import RPi.GPIO as GPIO
import socket

GPIO.cleanup()

ir_sensor = IRSensor.IRSensor(7)

motor = Motor.Motor(3,5,11,1000,5.0)

Motor.run(motor)

rpm = 0.0

'''
while rpm < 2000:
	rpm = IRSensor.read_rpm()
	time.sleep(1)
	print(rpm)
	Motor.changespeed(motor, motor.duty+0.1)
'''

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


time.sleep(10)
print("FUSK!")