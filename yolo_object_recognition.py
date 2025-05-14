from ultralytics import YOLO
import cv2
import requests
import numpy as np

# Load the YOLO model
model = YOLO('yolov8n.pt')

# Set your Pi's IP address and Flask stream URL
ip_address = input("Enter Raspberry Pi IP address: ")
url = f'http://{ip_address}:5000/video_feed'
print(f"Connecting to: {url}")
stream = requests.get(url, stream=True)

# Parse the MJPEG stream
bytes_data = b""
for chunk in stream.iter_content(chunk_size=1024):
    bytes_data += chunk
    a = bytes_data.find(b'\xff\xd8')  # JPEG start
    b = bytes_data.find(b'\xff\xd9')  # JPEG end
    if a != -1 and b != -1:
        jpg = bytes_data[a:b+2]
        bytes_data = bytes_data[b+2:]
        frame = cv2.imdecode(np.frombuffer(jpg, dtype=np.uint8), cv2.IMREAD_COLOR)

        # Run YOLO detection on the frame
        results = model.predict(frame, imgsz=640, conf=0.5, verbose=False)
        annotated_frame = results[0].plot()

        # Show the frame
        cv2.imshow("YOLOv8 Detection", annotated_frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cv2.destroyAllWindows()
