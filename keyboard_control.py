import curses #built in python library - lets user enter real-time keystrokes without waiting for 'enter'
from adafruit_motorkit import MotorKit #Requires the following bash command: sudo pip3 install adafruit-circuitpython-motorkit

"""
kit = MotorKit() is creating a connection to the HAT, and that connection is called kit.
If I may use an analogy, it is like main_window = Tk() creates a connection to a GUI, and
calling that connection main_window.

Then from there, MotorKit() contains built in attriubtues, such as .stepper or .motor.
If it's stepper, then you can control stepper1 and stepper2. If it's motor then you can
control from motor1 all the way to motor4. Each .motor maps to the terminal inputs that
the wires from the motors connect to.

.throttle is another built-in attribute of MotorKit(), and it takes a value from -1.0 to 1.0,
which determines how much PWM is sent to each motor.
"""

kit = MotorKit()
SPEED = 0.5 #Global variable to make speed adjustments for the functions a lot easier

"""
The following functions determine the spin direction of each of the 4 motors. Forward, backward,
left and right and fairly self-explanatory. The strafing logic is specific to mecanum wheel
geometry. The design of mecanum wheels means that when adjacent wheels spin against each other
it generates a lateral/strafing movement.
"""

def stop():
    for m in [kit.motor1, kit.motor2, kit.motor3, kit.motor4]:
        m.throttle = 0

def move_forward():
    kit.motor1.throttle = SPEED
    kit.motor2.throttle = SPEED
    kit.motor3.throttle = SPEED
    kit.motor4.throttle = SPEED

def move_backward():
    kit.motor1.throttle = -SPEED
    kit.motor2.throttle = -SPEED
    kit.motor3.throttle = -SPEED
    kit.motor4.throttle = -SPEED

def turn_left():
    kit.motor1.throttle = SPEED  * 1.5
    kit.motor2.throttle = SPEED * 1.5
    kit.motor3.throttle = -SPEED * 1.5
    kit.motor4.throttle = -SPEED  * 1.5

def turn_right():
    kit.motor1.throttle = -SPEED * 1.5
    kit.motor2.throttle = -SPEED * 1.5
    kit.motor3.throttle = SPEED * 1.5
    kit.motor4.throttle = SPEED * 1.5

def strafe_left():
    kit.motor1.throttle = SPEED * 2
    kit.motor2.throttle = -SPEED * 2
    kit.motor3.throttle = -SPEED * 2
    kit.motor4.throttle = SPEED * 2

def strafe_right():
    kit.motor1.throttle = -SPEED * 2
    kit.motor2.throttle = SPEED * 2
    kit.motor3.throttle = SPEED * 2
    kit.motor4.throttle = -SPEED * 2

"""
Curses is a built in library in python that lets you read real-time key presses in a 'curses terminal'.
By that I mean it is not the command line terminal, it is its own terminal. For instance, if you
used the print function, it would print to the command line terminal, but NOT to the curses terminal. To print
to the curses terminal, you need to use 'stdscr.addstr()'. I use this example to highlight that curses is creating
a new terminal from which you can run text-based programs (such as keyboard inputs to execute functions).

Using curses for this project allows me to create a 'GUI' of sorts from which I can use the keyboard to control
the robot, all from the comfort of the SSH. No need for HDMI-microHDMI cables, no fancy Raspberry Pi GUI, just
good old fashioned SSH and bash to run python scripts.
"""

def main(stdscr): #stdscr is 'standard screen'. So it's creating something outside the terminal, much like tkinter creates a
                  #GUI window outside the terminal.
    """
    These next 4 lines of code are basically the 'settings' for the curses terminal
    """
    stdscr.nodelay(True) #This allows smooth, continuous movement of the robot. Without it, the robot would move for a split second when a key is pressed, then it would stop and wait for the next key press.
    stdscr.clear() #This clears the screen every time the program is run - clean slate every time. Analagous to .delete(0, end) in Tkinter.
    stdscr.addstr("Controls:\nW/S = forward/backward\nA/D = turn\nQ/E = strafe\nSpace bar = stop\nX = quit\n") #This is basically 'print' except it prints to the stdscr instead of the terminal. addstr means add string.
    stdscr.refresh() #This line 'refreshes' the curses terminal. When .clear was called, it wiped the terminal clean. then addstr() printed text to that terminal. But for the text to be visible to the user the terminal needs to be refreshed so the updated info can be seen.

    """
    From here, we have the main-loop of the keyboard control logic. The while True loops allows continuous, real-time input handling.
    Each motor control function is assigned to a specific key on the keyboard (W,A,S,D,Q,E,X, Spacebar).

    """
    while True:
            key1 = stdscr.getch() #These 3 lines of code allowed the user to enter 2 key presses to allow
            key2 = stdscr.getch() #combos such as W + Q for diagonal movement. I eventually removed the
            keys = {key1, key2}   #diagonal movement from the if-else branches because they caused jittery
                                  #movement, however this structure remains for future use or expansion.

            if ord(' ') in keys:
                stop()
            elif ord('x') in keys:
                break
            elif ord('w') in keys:
                move_forward()
            elif ord('s') in keys:
                move_backward()
            elif ord('a') in keys:
                turn_left()
            elif ord('d') in keys:
                turn_right()
            elif ord('q') in keys:
                strafe_left()
            elif ord('e') in keys:
                strafe_right()
            elif -1 not in keys:
                stop()

curses.wrapper(main) #This is analagous to .mainloop() in Tkinter. It runs the curses terminal(interface) and executes the main(stdscr)
                     #function inside it. The .wrapper() method handles all the setup and cleanup for the curses terminal.
stop()
print("Exiting...")
