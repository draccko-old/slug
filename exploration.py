try:
    import RPi.GPIO as GPIO
    GPIO.setwarnings(False) # type: ignore
    # print("Current platform: Raspi.")
    status = True
except ImportError as e:
    # print("Libraries are broken / you aren't on a Raspi, error detected: ", e)
    status = False
import ultrasonic
import time
import figureCoords
import random
import wheelWriteThrowback

# nothing

startStamp = 0
if status: # init
    # Define GPIO pins for the left and right wheels
    leftWheel = 23
    rightWheel = 24
    
    # Set the GPIO mode to BCM
    GPIO.setmode(GPIO.BCM)
    
    # Set the motor pins as output
    GPIO.setup(leftWheel, GPIO.OUT)
    GPIO.setup(rightWheel, GPIO.OUT)
    
    # Setup PWM on the motor pins (e.g., 50Hz frequency)
    pwmLeft = GPIO.PWM(leftWheel, 50)  # 50Hz
    pwmRight = GPIO.PWM(rightWheel, 50)  # 50Hz
    
    # Start PWM with a duty cycle of 0 (motors off)
    pwmLeft.start(1)
    pwmRight.start(1)

currentDirection = 0  # Direction in degrees (0 = forward, 1 = right, etc.)
currentPosition = (0, 0)  # Starting position (x, y)
exploring = False # Flag to indicate if the robot is exploring



def explore():
    startTime = time.time()
    # print("Cycle started, pos:", currentPosition)
    while (startTime - time.time()) <= 1:      
        if ultrasonic.measureDistance() <= 30:
                ultrasonicDistance = ultrasonic.measureDistance()
                # print("Possible obstacle detected, checking...")
                if ultrasonicDistance > 0 and ultrasonicDistance < 30:
                    # print("Passed, avoiding...")
                    avoid()
                # else:
                    # print("Not valid, not avoiding...")
                        
        pwmLeft.ChangeDutyCycle(1)  # Adjust speed here (0-1)
        wheelWriteThrowback.writePWM(1, "left")    
        pwmRight.ChangeDutyCycle(10)  # Adjust speed here (0-1)
        wheelWriteThrowback.writePWM(1, "right")
    else:
        print("else")

def avoid():
    # print("Obstacle detected! Avoiding.   " + str(ultrasonic.measureDistance()))
    global currentDirection
    
    pwmLeft.ChangeDutyCycle(1)  # Adjust speed here (0-1)
    wheelWriteThrowback.writePWM(1, "left")
    pwmRight.ChangeDutyCycle(1)  # Adjust speed here (0-1)
    wheelWriteThrowback.writePWM(1, "right")
    time.sleep(5)  # Turn for 1 second
    pwmLeft.ChangeDutyCycle(10)
    wheelWriteThrowback.writePWM(10, "left")
    pwmRight.ChangeDutyCycle(1)
    wheelWriteThrowback.writePWM(1, "right")

def start():
    exploring = True  # Start exploring
    explore()
    pwmLeft.ChangeDutyCycle(1)
    wheelWriteThrowback.writePWM(1, "left")
      # Adjust speed here (0-1)
    pwmRight.ChangeDutyCycle(10)  # Adjust speed here (0-1)
    wheelWriteThrowback.writePWM(1, "right")

def stop():
    if status:
        exploring = False  # Stop exploring
        pwmLeft.ChangeDutyCycle(0)
        wheelWriteThrowback.writePWM(0, "left")
        pwmRight.ChangeDutyCycle(0)
        wheelWriteThrowback.writePWM(0, "right")
    return startStamp - time.time()

while exploring:
    explore()

while True:
    explore()