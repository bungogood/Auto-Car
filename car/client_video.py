from time import sleep, time
from socket import *
import picamera
import struct
import io

class SplitFrames(object):
    def __init__(self, connection):
        self.connection = connection
        self.stream = io.BytesIO()
        self.count = 0

    def write(self, buf):
        if buf.startswith(b"\xff\xd8"):
            size = self.stream.tell()
            if size > 0:
                self.connection.write(struct.pack("<L", size))
                self.connection.flush()
                self.stream.seek(0)
                self.connection.write(self.stream.read(size))
                self.count += 1
                self.stream.seek(0)
        self.stream.write(buf)

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(("192.168.0.38", 5001))
connection = client_socket.makefile("wb")

try:
    output = SplitFrames(connection)
    with picamera.PiCamera(resolution=(320,240), framerate=30) as camera:
        camera.rotation = 180
        sleep(2)
        start = time()
        camera.start_recording(output, format="mjpeg")
        camera.wait_recording(1200)
        camera.stop_recording()
except:
    pass
finally:
    print("Sent images: ", output.count)
    print("seconds: ", time() - start)
    print("fps: ", output.count / (time()-start))
    connection.close()
    client_socket.close()