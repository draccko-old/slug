import math

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
    while True():
        if 