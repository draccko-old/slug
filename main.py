import ultrasonic
import figureCoords  # type:ignore
import exploration  # type:ignore

mps = 0
explorating = True

print(ultrasonic.measure_distance())
print(figureCoords.getPointCoordinates(0, 1, 1, 90))

if explorating:
    exploration.currentDirection = 0  # Set initial direction (e.g., 0 degrees)
    exploration.explore()

