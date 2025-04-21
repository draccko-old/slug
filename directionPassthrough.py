direction = 0 # how tf do i wire a microbit to an rpi?????????

##k nvm i figured it out

    

try:
   import serial
    # Adjust the port if needed (e.g., ttyACM1)

except serial.SerialException as e:

    # print("Error opening serial port: ", e)
    ser = None


ser = serial.Serial('/dev/ttyACM0', 115200)
def getDirection():
    try:
        line = ser.readline().decode('utf-8').strip()
        print("Compass heading:", line)
        direction = line
    except serial.SerialException as e:
        print("Error reading from serial port: ", e)