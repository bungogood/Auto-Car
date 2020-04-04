import RPi.GPIO as GPIO

#7.5 left
#8.3 straight
#9 right

class Servo:
    def __init__(self, pin):
        GPIO.setup(pin, GPIO.OUT)
        self.pin = pin
        self.pwm = GPIO.PWM(pin, 50)
        self.pwm.start(0)
        self.straight()
    
    def left(self):
        self.pwm.ChangeDutyCycle(7.5)
    
    def straight(self):
        self.pwm.ChangeDutyCycle(8.3)
    
    def right(self):
        self.pwm.ChangeDutyCycle(9)