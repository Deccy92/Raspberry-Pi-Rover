# Raspberry Pi Autonomous Rover

An ongoing full-stack robotics project powered by a Raspberry Pi 4B, designed to explore remote control, AI vision, and embedded systems integration.

## 🚀 Features Implemented
- **Live video streaming** via Sony IMX500 AI Camera
- **Remote control** via SSH and Python curses
- **Object detection** using onboard MobileNet SSD on the camera's NPU
- **Wireless TCP/IP communication** for command and video streaming
- **Mecanum wheels** for omnidirectional movement

## 🔧 Technologies Used
- Python (Flask, subprocess, curses, Adafruit_MotorKit, blinka)
- Raspberry Pi OS (32-bit, Bookworm)
- Adafruit DC Motor HAT
- Waveshare UPS HAT (B)
- Raspberry Pi AI Camera (Sony IMX500 sensor)
- WebSockets / TCP-IP networking
- systemd (for boot-time service autostart)
- SSH remote access

## 🔭 Roadmap / In Progress
- ⏳ Add GPS module for location logging
- ⏳ Log detections to SQLite with timestamps and coordinates
- ⏳ Add LiDAR and implement SLAM
- ⏳ Develop autonomous navigation logic
- ⏳ Deploy to outdoor environments for plastic detection use case

## 🧠 Long-Term Goal
To create a self-navigating robot that detects plastic waste, logs it via GPS, and maps its surroundings using SLAM — forming the foundation of a scalable environmental cleanup system.


## 🧪 How to Use
1.	Boot the Pi – the Flask server starts automatically via systemd
2.	View Live Feed – open a browser on the same network: http://{pi-ip}:5000
3.	Control the Rover
   
    o	SSH into the Pi
  
    o	Type drive (custom alias to activate virtual environment and launch keyboard control)

    o	Use:

    	W/S to move forward/backward
    	A/D to turn
    	Q/E to strafe
    	Space to stop
    	X to quit


## 📷 Media
![Top Left view](rover1.png)
![Front view](rover2.png)
![Rear view](rover3.png)
![Left view](rover4.png)
![Right Side view](rover5.png)
![Hardware view](rover6.png)
![Top view](rover7.png)

## 👤 Author
**Declan Gregg**  
Bachelor of IT (Computer Science), QUT  
GitHub: [Deccy92](https://github.com/Deccy92)

