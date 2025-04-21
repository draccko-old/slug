import RPi.GPIO as GPIO
GPIO.setwarnings(False) # type: ignore

GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT)
wheel = GPIO.PWM(24, 50)
wheel.start(0)

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT)
wheel2 = GPIO.PWM(23, 50)
wheel2.start(0)

while True:
    wheel.ChangeDutyCycle(10)
    wheel2.ChangeDutyCycle(1)