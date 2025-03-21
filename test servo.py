import RPi.GPIO as GPIO
import time

# Set up the GPIO mode and pin
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

# Create a PWM instance for the servo control on GPIO17
servo = GPIO.PWM(17, 50)  # 50Hz PWM frequency

# Start PWM with 0% duty cycle (servo is not moving initially)
servo.start(0)



try:
    while True:
        servo.start(1)

except KeyboardInterrupt:
    print("Exiting program")

# Cleanup the GPIO settings before exiting
finally:
    servo.stop()
    GPIO.cleanup()
º