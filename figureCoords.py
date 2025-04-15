import math
import wheelWriteThrowback
import directionPassthrough

currentPosition = (0, 0)  # Starting position (x, y)


def getPointCoordinates(x0, y0, distance, angleDegrees):
    angleRadians = math.radians(angleDegrees)  # Convert angle to radians

    # Calculate new coordinates
    x = x0 + distance * math.cos(angleRadians)
    y = y0 + distance * math.sin(angleRadians)

    # Explicit rounding to avoid floating-point precision issues
    return round(x), round(y)

metrosPorSegundo = 2

def calcDistance(timeSeconds):
    return metrosPorSegundo * timeSeconds  # Calculate distance using speed (m/s) and time (s)


def listenOnWheelRuntime():
    while True:
        while wheelWriteThrowback.leftPWMValue == 90 and wheelWriteThrowback.rightPWMValue == 90:
            angleToRadians = math.radians(directionPassthrough.direction)
            currentPosition += (
                round(calcDistance(0.01) * math.cos(angleToRadians)),
                round(calcDistance(0.01) * math.sin(angleToRadians)),
            )

def init():
    global currentPosition
    currentPosition = (0, 0)  # Reset to starting position
    listenOnWheelRuntime()