from simulator import robot, FORWARD, BACKWARD, STOP
# TODO: Write your code here!
# Use robot.motors() to move
# Use robot.left_sonar() and robot.right_sonar() to sense obstacles
import time



def forward():
    """ Move the robot forward for a short duration."""
    robot.motors(left=FORWARD, right=FORWARD, seconds=0.1)
def stop():
    """ Stop the robot for a short duration."""
    robot.motors(left=STOP, right=STOP, seconds=0.05)
def turnright(duration):
    """ Turn the robot right for a specified duration."""
    robot.motors(left=FORWARD, right=BACKWARD, seconds = duration)
    stop()

start_time = time.time()

while True:
    left = robot.left_sonar()
    right = robot.right_sonar()
    

    if left < 40 or right < 40:
        stop()
        time.sleep(0.1)
        turnright(0.15)
    else:
        forward()

    time.sleep(0.1)
    
    if time.time() - start_time > 150:
        break
robot.exit()


