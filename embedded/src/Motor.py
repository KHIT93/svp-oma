import RPi.GPIO as GPIO
import time


class Motor:
	"""docstring for Motor"""
	def __init__(self, pwm_pin, standby_pin, direction_pin, frequency,duty):
		GPIO.setmode(GPIO.BOARD)
		self.pwm_pin = pwm_pin
		self.standby_pin = standby_pin
		self.direction_pin = direction_pin
		self.frequency = frequency
		self.duty = duty
		GPIO.setup(self.pwm_pin, GPIO.OUT)
		GPIO.setup(self.standby_pin, GPIO.OUT)
		self.pwm = GPIO.PWM(pwm_pin, frequency)

def run(motor):
	motor.pwm.start(motor.duty)
	GPIO.output(motor.standby_pin, 1)


def stop(motor):
	GPIO.output(motor.standby_pin, 0)

def changespeed(motor, new_duty): 
	motor.duty = new_duty
	motor.pwm.ChangeDutyCycle(motor.duty)

def brake(motor):
	motor.duty -= 1
	motor.pwm.ChangeDutyCycle(motor.duty)
