import RPi.GPIO as GPIO

#7 start
#7.5 stop
#8 reverse

class ESC:
    def __init__(self, pin):
        GPIO.setup(pin, GPIO.OUT)
        self.pin = pin
        self.pwm = GPIO.PWM(pin, 50)
        self.pwm.start(0)
        self.stop()
    
    def start(self):
        self.pwm.ChangeDutyCycle(7)
    
    def stop(self):
        self.pwm.ChangeDutyCycle(7.5)
    
    def reverse(self):
        self.pwm.ChangeDutyCycle(8)