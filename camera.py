from picamera2 import Picamera2
from libcamera import Transform
import io
from PIL import Image

class VideoCamera:
    def __init__(self):
        self.picam2 = Picamera2()
        self.picam2.configure(self.picam2.create_video_configuration(
            main={"format": "RGB888", "size": (640, 480)},
            transform=Transform(hflip=1)
        ))
        self.picam2.start()

    def get_frame(self):
        frame = self.picam2.capture_array()
        img = Image.fromarray(frame)
        buffer = io.BytesIO()
        img.save(buffer, format='JPEG')
        return buffer.getvalue()
