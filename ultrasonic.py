try:
    import RPi.GPIO as GPIO
    GPIO.setwarnings(False) #type:ignore
    print("Current platform: Raspi.    - us.py ")
    status = True
except ImportError as e:
    print("Libraries are broken / you aren't on a raspi, error detected: ", e)
    status  = False

import time
import random
import math


initialised = False

if status and initialised == False:
    trig = 27
    echo = 22
    
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(trig, GPIO.OUT)
    GPIO.setup(echo, GPIO.IN)
    print("Ultrasonic sensor initialized.")
    initialised = True
else:
    print("Didnt init GPIO, already did it.")

def measureDistance():
    if status:
        # Send a pulse to trigger the sensor
        GPIO.output(trig, GPIO.LOW)
        GPIO.output(trig, GPIO.HIGH)
        time.sleep(0.01)
        GPIO.output(trig, GPIO.LOW)

        # Wait for the response from the sensor
        pulseStart = 0
        pulseEnd = 0

        # Wait until the echo pin goes HIGH
        while GPIO.input(echo) == GPIO.LOW:
            pulseStart = time.time()  # Capture the time when the pulse is LO
            if time.time() - pulseStart > 0.01:  # Timeout after 1 second
                return -1


            
        # Wait until the echo pin goes LOW
        while GPIO.input(echo) == GPIO.HIGH:
            pulseEnd = time.time()  # Capture the time when the pulse goes HIGH
            if time.time() - pulseStart > 0.01:  # Timeout after 1 second
                return -1

        # If either pulseStart or pulseEnd is still 0, there's an issue with the sensor
        if pulseStart == 0 or pulseEnd == 0: 
            return -1  # Return -1 to indicate an error in reading

        # Calculate the distance based on time
        pulseDuration = pulseEnd - pulseStart
        distance = pulseDuration * 17150  # Speed of sound in cm/s
        distance = clamp(distance, 0, 200)# Round to two decimal places
        
        # print("Distance: ", distance, "cm")
        if distance > 1:
            return distance
        else:
            # print("Distance too small, returning -1")
            return -1
        return distance
    else:
        # print("Not on a Raspi, returning random distance.")
        return random.randrange(10, 170) # Simulate a distance for testing
    

def clamp(n, smallest, largest): return max(smallest, min(n, largest))