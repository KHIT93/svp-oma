import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BOARD)

class ADC(object):
        """docstring for ADC"""
        def __init__(self, adcnum, clock_pin, miso_pin, mosi_pin, cs_pin):
                self.adcnum = adcnum
                self.clock_pin = clock_pin
                self.miso_pin = miso_pin
                self.mosi_pin = mosi_pin
                self.cs_pin = cs_pin

                # set up the interface pins
                GPIO.setup(mosi_pin, GPIO.OUT)
                GPIO.setup(miso_pin, GPIO.IN)
                GPIO.setup(clock_pin, GPIO.OUT)
                GPIO.setup(cs_pin, GPIO.OUT)

# read SPI data from MCP3008 chip, 8 possible adc's (0 thru 7)
def readadc(self):
        # Only between 0 and 7 ADC pins
        if ((self.adcnum > 7) or (self.adcnum < 0)):
                return -1

        GPIO.output(self.cs_pin, True)
        GPIO.output(self.clock_pin, False)  # start clock low
        GPIO.output(self.cs_pin, False)     # bring CS low
 
        commandout = self.adcnum
        commandout |= 0x18  # start bit + single-ended bit
        commandout <<= 3    # Only 5 bits needed here
        for i in range(5):
                if (commandout & 0x80):
                        GPIO.output(self.mosi_pin, True)
                else:
                        GPIO.output(self.mosi_pin, False)
                commandout <<= 1
                GPIO.output(self.clock_pin, True)
                GPIO.output(self.clock_pin, False)
 
        adcout = 0
        # read in one empty bit, one null bit and 10 ADC bits
        for i in range(12):
                GPIO.output(self.clock_pin, True)
                GPIO.output(self.clock_pin, False)
                adcout <<= 1
                if (GPIO.input(self.miso_pin)):
                        adcout |= 0x1
 
        GPIO.output(self.cs_pin, True)
        
        adcout >>= 1       # first bit is 'null' so drop it
        return adcout

def readtemperature(self):
        value = readadc(self)
        # Take the reading and multiply it by the volts on the ADC. Then divide by the amount of bits from the ADC
        volts = (value * 3.3) / 1024
        temperature = volts / (10.0 / 1000)

        return temperature