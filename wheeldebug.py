import RPi.GPIO as GPIO # type: ignore

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
wheel = GPIO.PWM(17, 50)

while True:
    wheel.start(0)
    wheel.ChangeDutyCycle(100)