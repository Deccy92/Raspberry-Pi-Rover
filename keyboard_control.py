import curses
from adafruit_motorkit import MotorKit

kit = MotorKit()
SPEED = 0.5

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
    kit.motor1.throttle = SPEED
    kit.motor2.throttle = SPEED
    kit.motor3.throttle = -SPEED
    kit.motor4.throttle = -SPEED

def turn_right():
    kit.motor1.throttle = -SPEED
    kit.motor2.throttle = -SPEED
    kit.motor3.throttle = SPEED
    kit.motor4.throttle = SPEED

def strafe_left():
    kit.motor1.throttle = SPEED
    kit.motor2.throttle = -SPEED
    kit.motor3.throttle = -SPEED
    kit.motor4.throttle = SPEED

def strafe_right():
    kit.motor1.throttle = -SPEED
    kit.motor2.throttle = SPEED
    kit.motor3.throttle = SPEED
    kit.motor4.throttle = -SPEED

def forward_left():
    kit.motor1.throttle = SPEED
    kit.motor2.throttle = SPEED
    kit.motor3.throttle = SPEED
    kit.motor4.throttle = SPEED

def forward_right():
    kit.motor1.throttle = SPEED
    kit.motor2.throttle = SPEED
    kit.motor3.throttle = SPEED
    kit.motor4.throttle = SPEED

def backward_left():
    kit.motor1.throttle = -SPEED
    kit.motor2.throttle = -SPEED
    kit.motor3.throttle = -SPEED
    kit.motor4.throttle = -SPEED

def backward_right():
    kit.motor1.throttle = -SPEED
    kit.motor2.throttle = -SPEED
    kit.motor3.throttle = -SPEED
    kit.motor4.throttle = -SPEED

def main(stdscr):
    stdscr.nodelay(True)
    stdscr.clear()
    stdscr.addstr("WASD to move, Q/E to strafe, diagonals = WA/WD/etc., X to quit\n")
    stdscr.refresh()

    while True:
        key1 = stdscr.getch()
        key2 = stdscr.getch()
        keys = {key1, key2}

        if ord('x') in keys:
            break
        elif ord('w') in keys and ord('a') in keys:
            forward_left()
        elif ord('w') in keys and ord('d') in keys:
            forward_right()
        elif ord('s') in keys and ord('a') in keys:
            backward_left()
        elif ord('s') in keys and ord('d') in keys:
            backward_right()
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

curses.wrapper(main)
stop()
print("Exiting...")
