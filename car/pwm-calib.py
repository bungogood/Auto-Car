from time import sleep
from RPi import GPIO
from sys import argv

#pwm calibration

if len(argv) == 3:
    _, pin, dc = argv
    t = 1000
elif len(argv) == 4:
    _, pin, dc, t = argv
else:
    raise AssertionError("must provide pin and duty cycle")

pin, dc, t = int(pin), float(dc), int(t)

try:
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin, GPIO.OUT)
    pwm = GPIO.PWM(pin, 50)
    pwm.start(0)
    sleep(3)
    pwm.ChangeDutyCycle(dc)
    sleep(t)
except KeyboardInterrupt:
    pass
finally:
    print()
    GPIO.cleanup()