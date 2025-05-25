from flask import Flask, render_template, Response #Flask creates the server, render_template loads the HTML file, Response streams the video
from camera import VideoCamera #Imports the VideoCamera class from my camera.py script

"""
app = Flask(__name__) initialises the Flask server. 'App' is the conventional variable name used (technically you could name it anything).
This is analagous to main_window = Tk(). This creates an instance of a Tkinter GUI and stores it in a variable called main_window which you
can then build on.

__name__ is a special Python variable that tells Flask which module is running. Flask, by design, then uses that to determine the
root path of the project. Flask, again by design, assumes that all the other necessary modules for the project will be in this root
folder and will begin searching for them. By default, Flask will search for a folder called templates and use it to load HTML files.

@app.route('/') is a route 'decorator' that tells Flask to run the function index(). The index function then returns render_template('index.html'),
which tells Flask to serve the file templates/index.html.
"""

app = Flask(__name__)
camera = VideoCamera()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    def gen():
        while True:
            frame = camera.get_frame()
            if frame:
                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
    return Response(gen(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000) #Port 5000 is Flask's default port
