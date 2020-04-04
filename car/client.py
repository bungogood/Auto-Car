from handler import *
import socketserver
import threading
import queue

class Client(object):
    def __init__(self, host, port_video):
        self.host = host
        self.port_video = port_video
    
    def video_stream(self, host, port, drive_queue):
        s = socketserver.TCPServer((host, port), VideoStreamHandler)
        s.drive_queue = drive_queue
        s.serve_forever()
    
    def start_thread(self, f, args):
        thread = threading.Thread(target=f, args=args)
        thread.daemon = True
        thread.start()
    
    def start(self):
        drive_queue = queue.PriorityQueue()
        self.start_thread(self.video_stream, (self.host, self.port_video, drive_queue))
        #self.start_thread(self.video_stream, (self.host, self.port_video, drive_queue))
        #self.start_thread(self.video_stream, (self.host, self.port_video, drive_queue))

c = Client(host="192.168.0.24", port_video=5001)
try:
    c.start()
except KeyboardInterrupt:
    pass

#s = socketserver.TCPServer(("192.168.0.38", 5001), VideoStreamHandler)
#s.serve_forever()

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