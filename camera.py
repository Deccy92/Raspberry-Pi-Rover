import subprocess

class VideoCamera:
    def __init__(self):
        self.process = subprocess.Popen(
            [
                "rpicam-vid",
                "-t", "0",  # Run indefinitely
                "--post-process-file", "/usr/share/rpi-camera-assets/imx500_mobilenet_ssd.json",
                "--codec", "mjpeg",
                "-o", "-"
            ],
            stdout=subprocess.PIPE
        )
        self.buffer = b""

    def get_frame(self):
        # Collect data until a full JPEG frame is found
        while True:
            chunk = self.process.stdout.read(1024)
            if not chunk:
                break
            self.buffer += chunk
            start = self.buffer.find(b'\xff\xd8')  # JPEG start
            end = self.buffer.find(b'\xff\xd9')    # JPEG end
            if start != -1 and end != -1 and end > start:
                frame = self.buffer[start:end+2]
                self.buffer = self.buffer[end+2:]  # Trim processed frame
                return frame
        return None

    def __del__(self):
        if self.process:
            self.process.terminate()
