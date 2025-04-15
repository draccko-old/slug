import ultrasonic
import figureCoords  # type:ignore
import exploration  # type:ignore
import time  # type:ignore
from slug import *

print(ultrasonic.measure_distance())
print(figureCoords.getPointCoordinates(0, 1, 1, 90))
startStamp = time.Time()
while True():
    while time.Time - startStamp <= 600:
        exploration.exploring = True
    while time.Time - startStamp >= 600 :
        exploration.exploring = False
    

