try:
    import RPi.GPIO as GPIO #type:ignore
    print("Current platform: Raspi.")
    status = True
except ImportError as e:
    print("Libraries are broken / you aren't on a raspi, error detected: ", e)
    status  = False

import time
import random

if status:
    # Set up GPIO pins
    TRIG = 24
    ECHO = 23
    
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.setup(ECHO, GPIO.IN)

def measure_distance():
    if status:
        # Send a pulse to trigger the sensor
        GPIO.output(TRIG, GPIO.LOW)
        time.sleep(0.5)
        GPIO.output(TRIG, GPIO.HIGH)
        time.sleep(0.00001)
        GPIO.output(TRIG, GPIO.LOW)

        # Wait for the response from the sensor
        pulse_start = 0
        pulse_end = 0

        # Wait until the ECHO pin goes HIGH
        while GPIO.input(ECHO) == GPIO.LOW:
            pulse_start = time.time()  # Capture the time when the pulse is LOW

        # Wait until the ECHO pin goes LOW
        while GPIO.input(ECHO) == GPIO.HIGH:
            pulse_end = time.time()  # Capture the time when the pulse goes HIGH

        # If either pulse_start or pulse_end is still 0, there's an issue with the sensor
        if pulse_start == 0 or pulse_end == 0:
            return -1  # Return -1 to indicate an error in reading

        # Calculate the distance based on time
        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * 17150  # Speed of sound in cm/s
        distance = round(distance, 2)  # Round to two decimal places

        return distance
    else:
        return random.randrange(10, 3000)