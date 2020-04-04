class Car:
    def __init__(self, port, esc_pin, Servo_pin):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        self.esc = ESC(esc_pin)
        self.servo = Servo(servo_pin)
        time.sleep(3)
    
    def steer():
        pass

    def speed():
        pass

    def left():
        pass

    def right():
        pass

    def stop():
        pass

class ESC:
    def init_ESC(self, pin):
        GPIO.setup(pin, GPIO.OUT)
        self.pin = pin
        self.esc = GPIO.PWM(pin, 50)
        self.esc.start(0)
        self.esc.ChangeDutyCycle(7.5)

class Servo:
    def __init__(self, pin):
        GPIO.setup(pin, GPIO.OUT)
        self.pin = pin
        self.servo = GPIO.PWM(pin, 50)
        self.servo.start(0)
        self.servo.ChangeDutyCycle(7.5)
