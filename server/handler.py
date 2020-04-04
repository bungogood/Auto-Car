import socketserver
import cv2
import numpy as np

class VideoStreamHandler(socketserver.StreamRequestHandler):
    def handle(self):
        stream_bytes = b' '
        try:
            while True:
                stream_bytes += self.rfile.read(1024)
                first = stream_bytes.find(b'\xff\xd8')
                last = stream_bytes.find(b'\xff\xd9')
                if first != -1 and last != -1:
                    jpg = stream_bytes[first:last + 2]
                    stream_bytes = stream_bytes[last + 2:]
                    image = self.image(jpg)
                    gray = self.gray(image)
                    gray = gray[130:320, :]
                    blur = self.blur(gray)
                    canny = self.canny(blur)
                    lines = cv2.HoughLinesP(canny,1,np.pi/180,20,minLineLength=60,maxLineGap=30)
                    imgls = add_lines(canny, lines)
                    #gray = cv2.imdecode(np.frombuffer(jpg, dtype=np.uint8), cv2.IMREAD_GRAYSCALE)
                    #image = cv2.imdecode(np.frombuffer(jpg, dtype=np.uint8), cv2.IMREAD_COLOR)
                    cv2.imshow('image', image)
                    cv2.imshow('canny', canny)
                    cv2.imshow('lines', imgls)
                    #height, width = gray.shape
                    #roi = gray[int(height/2):height, :]
                    #image_array = roi.reshape(1, int(height/2) * width).astype(np.float32)
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break
        finally:
            cv2.destroyAllWindows()

    def image(self, jpg):
        return cv2.imdecode(np.frombuffer(jpg, dtype=np.uint8), cv2.IMREAD_COLOR)
    
    def gray(self, image):
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    def blur(self, gray):
        #return cv2.GaussianBlur(gray, (5, 5), 0)
        return cv2.GaussianBlur(gray, (7, 7), 0)
    
    def canny(self, blur):
        return cv2.Canny(blur, 50, 150)

def add_lines(image, lines):
    line_image = np.zeros_like(image)
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line.reshape(4)
            cv2.line(line_image, (x1, y1), (x2, y2), 255, 10)
    return line_image