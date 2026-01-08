from simulator import robot, FORWARD, BACKWARD, STOP
# TODO: Write your code here!
# Use robot.motors() to move
# Use robot.left_sonar() and robot.right_sonar() to sense obstacles
import time


turn_direction = input("Turn left or right when obstacle detected (left/right)? ")
x = int(input("Set the sonar sensitivity (recomended minimum 30): "))
y = int(input("Set the maximum number of obstacles before the robot gets tired of you "))
obstacle_count = 0

def user_wants_to_quit():
    """ Check if the user wants to quit based on the user input."""
    if user_input == "q":
        return True
    else:
        return False
def forward():
    """ Move the robot forward for a short duration. or until uther commanded is given"""
    robot.motors(left=FORWARD, right=FORWARD, seconds=0.5)
def stop():
    """ Stop the robot for a specified duration."""
    robot.motors(left=STOP, right=STOP, seconds=0.05)
def turn(duration):
    """ Turn the robot a direction specified by user input for a specified duration."""
    if turn_direction == "right":
        robot.motors(left=BACKWARD, right=FORWARD, seconds = duration)
    else:   
        robot.motors(left=FORWARD, right=BACKWARD, seconds = duration)
        stop()

start_time = time.time()
last_asked_time = start_time

while True:
    left = robot.left_sonar()
    right = robot.right_sonar()
    

    if left < x or right < x:
        stop()
        turn(0.5)
    else:
        forward()

    if left < x or right < x:
        obstacle_count += 1
        print("Obstacles detected:", obstacle_count)
    if obstacle_count >= y:
        print("This space is too Complicated for me!!!!!")
        robot.exit()
    
    if time.time() - last_asked_time > 120:
        user_input = input("Continue (c) or Quit (q)? ")
        last_asked_time = time.time()
        def user_wants_to_quit():
            if user_input == "q":
                return True
            elif user_input == "c":
                return False
            else:
                print("Invalid input, please enter 'c' to continue or 'q' to quit.")
        if user_wants_to_quit():
            robot.exit()
            



