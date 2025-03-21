import RPi.GPIO as GPIO
import time

# Set up GPIO pins
TRIG = 24
ECHO = 23
LED_PIN = 25

GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(LED_PIN, GPIO.OUT)

# Set up PWM on LED_PIN with a frequency of 1000Hz
led_pwm = GPIO.PWM(LED_PIN, 1000)
led_pwm.start(0)  # Start with the LED off (0% duty cycle)

def measure_distance():
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

def adjust_led_brightness(distance):
    if distance == -1:
        led_pwm.ChangeDutyCycle(0)  # Turn off the LED if there's an error
    else:
        # Map the distance to a PWM duty cycle (0 to 100)
        # Close distance -> high brightness, far distance -> low brightness
        max_distance = 200  # Maximum measurable distance (adjust as needed)
        min_distance = 10   # Minimum measurable distance (adjust as needed)

        # Ensure the distance is within the valid range
        if distance < min_distance:
            distance = min_distance
        if distance > max_distance:
            distance = max_distance

        # Map distance to PWM duty cycle (inverse: closer = brighter)
        brightness = ((max_distance - distance) / (max_distance - min_distance)) * 100
        led_pwm.ChangeDutyCycle(brightness)

try:
    print("Startup...")
    while True:
        distance = measure_distance()
        print(f"Distance: {distance} cm")
        adjust_led_brightness(distance)  # Adjust LED brightness based on the distance
        time.sleep(0.1)

except KeyboardInterrupt:
    print("Measurement stopped by user")
    led_pwm.stop()  # Stop PWM on exit
    GPIO.cleanup()
