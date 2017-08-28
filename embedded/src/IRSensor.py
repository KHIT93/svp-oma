import RPi.GPIO as GPIO
import time
from multiprocessing.dummy import Pool as ThreadPool 



class IRSensor:
	"""docstring for IRSensor"""
	def __init__(self, ir_pin):
		self.ir_pin = ir_pin
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(ir_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
		GPIO.add_event_detect(ir_pin, GPIO.FALLING, callback=callback, bouncetime=10)

	
	def read_rpm(self):
		global count
		global last_time

		local_count = count
		local_time = last_time
		time_now = time.perf_counter()

		last_time = time.perf_counter()
		count = 0
		local_count = local_count * 0.5
		time_since = time_now - local_time
		seconds = 60.0 / time_since
		rpm = local_count * seconds
		return rpm

count = 0
last_time = time.perf_counter()
	
def callback(channel):
	global count
	count += 1