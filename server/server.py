from handler import *
import socketserver
import threading
import queue

class Server(object):
    def __init__(self, host, port_video):
        self.host = host
        self.port_video = port_video
        #self.port_sensor = port_sensor
        #self.port_drive = port_drive
    
    def video_stream(self, host, port, drive_queue):
        s = socketserver.TCPServer((host, port), VideoStreamHandler)
        s.drive_queue = drive_queue
        s.serve_forever()
    
    def sensor_stream(self, host, port, drive_queue):
        s = socketserver.TCPServer((host, port), SensorDataHandler)
        s.drive_queue = drive_queue
        s.serve_forever()
    
    def drive_stream(self, host, port, drive_queue):
        s = socketserver.TCPServer((host, port), UserDriveHandler)
        s.drive_queue = drive_queue
        s.serve_forever()
    
    def start_thread(self, f, args):
        thread = threading.Thread(target=f, args=args)
        thread.daemon = True
        thread.start()
    
    def start(self):
        drive_queue = queue.PriorityQueue()
        self.video_stream(self.host, self.port_video, drive_queue)
        #self.start_thread(self.video_stream, (self.host, self.port_video, drive_queue))
        #sensor_thread = threading.Thread(target=self.sensor_stream, args=(self.host, self.port_sensor, drive_queue))
        #sensor_thread.daemon = True
        #sensor_thread.start()
        #video_thread = threading.Thread(target=self.video_stream, args=(self.host, self.port_video, drive_queue))
        #video_thread.daemon = True
        #video_thread.start()
        #self.drive_stream(self.host, self.port_drive, drive_queue)

s = Server(host="192.168.0.24", port_video=5001)
try:
    s.start()
except:
    pass

#s = socketserver.TCPServer(("192.168.0.38", 5001), VideoStreamHandler)
#s.serve_forever()