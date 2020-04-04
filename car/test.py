from time import sleep
from RPi import GPIO
from ultra import *
from servo import *
from ESC import *

trg_pin = 15
ech_pin = 13
srv_pin = 11
esc_pin = 7

try:
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    srv = Servo(srv_pin)
    esc = ESC(esc_pin)
    ult = Ultra(trg_pin, ech_pin)
    sleep(3)
    '''
    esc.start()
    sleep(2)
    esc.stop()
    '''
    while True:
        srv.left()
        sleep(2)
        srv.right()
        sleep(2)
        srv.straight()
        sleep(2)
except KeyboardInterrupt:
    pass
finally:
    print()
    GPIO.cleanup()