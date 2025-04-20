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
    trig = 24
    echo = 23
    
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(trig, GPIO.OUT)
    GPIO.setup(echo, GPIO.IN)

def measureDistance():
    if status:
        # Send a pulse to trigger the sensor
        GPIO.output(trig, GPIO.LOW)
        time.sleep(0.5)
        GPIO.output(trig, GPIO.HIGH)
        time.sleep(0.00001)
        GPIO.output(trig, GPIO.LOW)

        # Wait for the response from the sensor
        pulseStart = 0
        pulseEnd = 0

        # Wait until the echo pin goes HIGH
        while GPIO.input(echo) == GPIO.LOW:
            pulseStart = time.time()  # Capture the time when the pulse is LOW

        # Wait until the echo pin goes LOW
        while GPIO.input(echo) == GPIO.HIGH:
            pulseEnd = time.time()  # Capture the time when the pulse goes HIGH

        # If either pulseStart or pulseEnd is still 0, there's an issue with the sensor
        if pulseStart == 0 or pulseEnd == 0: 
            return -1  # Return -1 to indicate an error in reading

        # Calculate the distance based on time
        pulseDuration = pulseEnd - pulseStart
        distance = pulseDuration * 17150  # Speed of sound in cm/s
        distance = round(distance, 2)  # Round to two decimal places

        return distance
    else:
        return random.randrange(10, 3000)