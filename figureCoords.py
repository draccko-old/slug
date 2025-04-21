import math
import wheelWriteThrowback
import directionPassthrough
import time
import threading

currentPosition = (0, 0)  # Initial position (x, y) in meters
print("figureCoords imported and thread will start")

def getPointCoordinates(x0, y0, distance, angleDegrees):
    angleRadians = math.radians(angleDegrees)  # Convert angle to radians
    x = x0 + distance * math.cos(angleRadians)
    y = y0 + distance * math.sin(angleRadians)
    return round(x), round(y)

metrosPorSegundo = 2

def calcDistance(timeSeconds):
    return metrosPorSegundo * timeSeconds

def listenOnWheelRuntime():
    global currentPosition
    while True:
        print("Recording position at" + time.strftime("%H:%M:%S") + "      " + "dir: " + str(directionPassthrough.direction) + " wwt left" + str(wheelWriteThrowback.leftPWMValue) + " right: " + str(wheelWriteThrowback.rightPWMValue), end="\r\r")
        angleToRadians = math.radians(directionPassthrough.direction)
        currentPosition = (
            currentPosition[0] + round(calcDistance(0.01) * math.cos(angleToRadians)),
            currentPosition[1] + round(calcDistance(0.01) * math.sin(angleToRadians)),
        )
        #if wheelWriteThrowback.leftPWMValue < 9 and wheelWriteThrowback.rightPWMValue > 9:
        time.sleep(0.01)
        print("Current position:", currentPosition, end="\r")  # Print the current position without a newline

# Start the loop in a daemon thread so it doesn't block or hang the parent script
listener_thread = threading.Thread(target=listenOnWheelRuntime, daemon=True)
listener_thread.start()
