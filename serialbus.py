import serial
microbit_serial = serial.Serial('/dev/ttyACM0', 115200, timeout = .1)

while True:
    global direction
    try:
        direction = float(microbit_serial.readline().decode('utf-8').strip())
    except ValueError as e:
        # print("Empty connection.: ", e)
        break