import ultrasonic
import figureCoords #type:ignore
import exploration #type:ignore

print(ultrasonic.measure_distance())
print(figureCoords.get_point_coordinates(0, 1, 1, 90))


explorating = True
while explorating:
    exploration.explore()