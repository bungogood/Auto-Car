from picamera import PiCamera
from sys import argv

assert len(argv) == 2, "no filename"

with PiCamera() as camera:
    camera.rotation = 180
    camera.resolution = (320, 240)
    camera.capture("/home/pi/Pictures/{}.jpg".format(argv[1]))