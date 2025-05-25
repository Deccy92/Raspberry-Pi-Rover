import subprocess

"""
subprocess is a python module that allows the programmer to run linux shell commands inside the python script.
This allows low-level hardware interaction with fast and effective linux commands.

The main subprocess funciton used in this program is:
    'subprocess.Popen()' - executes a command and lets the program interact with it while it is running - this enables continuous access to its output.
"""

class VideoCamera: #This is defining a class called VideoCamera
    def __init__(self): #This constructor function is called whenever a program creates a VideoCamera object, executing the below code
        self.process = subprocess.Popen(
            [
                "rpicam-vid", #Starts the video capture
                "-t", "0",  #Tells the camera to run indefinitely
                "--post-process-file", "/usr/share/rpi-camera-assets/imx500_mobilenet_ssd.json", #This command is taken straight from the Raspberry Pi AI Camera documentation - it runs rpicam-vid with object detection post-processing
                "--codec", "mjpeg", #This tells the camera to encode the data as mjpeg
                "-o", "-" #Sends the stream directly to stdout (standard output), not a file
            ],
            stdout=subprocess.PIPE #Captures the output so Python can read it as a live stream
        )
        self.buffer = b"" #A byte buffer to store incoming stream data and extract full JPEGs

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


