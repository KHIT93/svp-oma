import RPi.GPIO as GPIO
import time


class Motor:
	"""docstring for Motor"""
	def __init__(self, pwm_pin, standby_pin, direction_pin, frequency, duty):
		GPIO.setmode(GPIO.BOARD)
		self.pwm_pin = pwm_pin
		self.standby_pin = standby_pin
		self.direction_pin = direction_pin
		self.frequency = frequency
		self.duty = duty
		GPIO.setup(self.pwm_pin, GPIO.OUT)
		GPIO.setup(self.standby_pin, GPIO.OUT)
		GPIO.setup(self.direction_pin, GPIO.OUT)
		self.pwm = GPIO.PWM(pwm_pin, frequency)

	def run(self):
		self.pwm.start(self.duty)
		GPIO.output(self.standby_pin, 1)
		GPIO.output(self.direction_pin, 1)


	def stop(self):
		GPIO.output(self.standby_pin, 0)

	def changespeed(self, wind_speed, wing_angle): 
		self.duty = wind_speed - wing_angle
		self.pwm.ChangeDutyCycle(self.duty)

	def brake(self):
		self.duty -= 10
		self.pwm.ChangeDutyCycle(self.duty)
