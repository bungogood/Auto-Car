from time import sleep, time
from RPi import GPIO
from time import sleep

class Car:
    def __init__(self, esc_pin, srv_pin, trg_pin, ech_pin):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        self.esc = ESC(esc_pin)
        self.srv = Servo(srv_pin)
        self.ult = Ultra(trg_pin, ech_pin)
        sleep(3)
    
    def end(self):
        GPIO.cleanup()

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