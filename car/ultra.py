from time import sleep, time
import RPi.GPIO as GPIO

class Ultra:
    def __init__(self, trig, echo):
        GPIO.setup(trig, GPIO.OUT)
        GPIO.setup(echo, GPIO.IN)
        GPIO.output(trig, False)
        self.trig = trig
        self.echo = echo
    
    def dist(self):
        GPIO.output(self.trig, True)
        sleep(0.00001)
        GPIO.output(self.trig, False)
        while not GPIO.input(self.echo):
            start = time()
        while GPIO.input(self.echo):
            end = time()
        return round((end-start)*171500)