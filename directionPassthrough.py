direction = 0 # how tf do i wire a microbit to an rpi?????????

#k nvm i figured it out

import serial

# Adjust the port if needed (e.g., ttyACM1)
ser = serial.Serial('/dev/ttyACM0', 115200)

while True:
    line = ser.readline().decode('utf-8').strip()
    print("Compass heading:", line)
    direction = line