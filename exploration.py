try:
    import RPi.GPIO as GPIO # type: ignore
    print("Current platform: Raspi.")
    status = True
except ImportError as e:
    print("Libraries are broken / you aren't on a Raspi, error detected: ", e)
    status = False
import ultrasonic
import time

if status:
    # Define GPIO pins for the left and right wheels
    leftWheel = 12
    rightWheel = 16
    
    # Set the GPIO mode to BCM
    GPIO.setmode(GPIO.BCM)
    
    # Set the motor pins as output
    GPIO.setup(leftWheel, GPIO.OUT)
    GPIO.setup(rightWheel, GPIO.OUT)
    
    # Setup PWM on the motor pins (e.g., 50Hz frequency)
    pwm_left = GPIO.PWM(leftWheel, 50)  # 50Hz
    pwm_right = GPIO.PWM(rightWheel, 50)  # 50Hz
    
    # Start PWM with a duty cycle of 0 (motors off)
    pwm_left.start(0)
    pwm_right.start(0)

def explore():
    if status:
        if ultrasonic.measure_distance() < 20:
            # Set PWM duty cycle to turn motors on. 
            # Adjust the duty cycle (0-100) for speed control.
            
            # Move forward
            pwm_left.ChangeDutyCycle(90)  # Adjust speed here (0-100)
            pwm_right.ChangeDutyCycle(-90)  # Adjust speed here (0-100)
        else:
            pwm_left.ChangeDutyCycle(90)  # Adjust speed here (0-100)
            pwm_right.ChangeDutyCycle(90) # Adjust speed here (0-100)
            
    else:
        print("Cannot start exploration right now, not on real hardware.")

def stop():
    if status:
        pwm_left.ChangeDutyCycle(0)
        pwm_right.ChangeDutyCycle(0)
