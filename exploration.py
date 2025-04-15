try:
    import RPi.GPIO as GPIO # type: ignore
    print("Current platform: Raspi.")
    status = True
except ImportError as e:
    print("Libraries are broken / you aren't on a Raspi, error detected: ", e)
    status = False
import ultrasonic
import time
import figureCoords
import random
import wheelWriteThrowback


startStamp = 0

if status: # init
    # Define GPIO pins for the left and right wheels
    leftWheel = 12
    rightWheel = 16
    
    # Set the GPIO mode to BCM
    GPIO.setmode(GPIO.BCM)
    
    # Set the motor pins as output
    GPIO.setup(leftWheel, GPIO.OUT)
    GPIO.setup(rightWheel, GPIO.OUT)
    
    # Setup PWM on the motor pins (e.g., 50Hz frequency)
    pwmLeft = GPIO.PWM(leftWheel, 50)  # 50Hz
    pwmRight = GPIO.PWM(rightWheel, 50)  # 50Hz
    
    # Start PWM with a duty cycle of 0 (motors off)
    pwmLeft.start(0)
    pwmRight.start(0)

currentDirection = 0  # Direction in degrees (0 = forward, 90 = right, etc.)
currentPosition = (0, 0)  # Starting position (x, y)
exploring = True # Flag to indicate if the robot is exploring



def explore():
    oneSecondCicle() # i dont know what i was thinking when i overcomplicated this so much

def oneSecondCicle():
    progressTime = time.time()
    while progressTime - time.time >= 1:      
        pwmLeft.ChangeDutyCycle(90)  # Adjust speed here (0-100)
        wheelWriteThrowback.writePWM(90, "left")    
        pwmRight.ChangeDutyCycle(90)  # Adjust speed here (0-100)
        wheelWriteThrowback.writePWM(90, "right")
        if ultrasonic.measure_distance() <= 30:
                progressTime -= 2
                avoid()
    print("holy crap i actually did it")
    
def avoid():
    global currentDirection
    
    pwmLeft.ChangeDutyCycle(90)  # Adjust speed here (0-100)
    wheelWriteThrowback.writePWM(90, "left")
    pwmRight.ChangeDutyCycle(-90)  # Adjust speed here (0-100)
    wheelWriteThrowback.writePWM(-90, "right")
    time.sleep(2)  # Turn for 1 second
    pwmLeft.ChangeDutyCycle(0)
    wheelWriteThrowback.writePWM(0, "left")
    pwmRight.ChangeDutyCycle(0)
    wheelWriteThrowback.writePWM(0, "right")

def start():
    exploring = True  # Start exploring
    pwmLeft.ChangeDutyCycle(90)
    wheelWriteThrowback.writePWM(90, "left")
      # Adjust speed here (0-100)
    pwmRight.ChangeDutyCycle(90)  # Adjust speed here (0-100)
    wheelWriteThrowback.writePWM(90, "right")

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
while not exploring:
    stop()
    print("Exploration stopped.")