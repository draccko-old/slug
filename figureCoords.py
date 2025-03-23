import math

def get_point_coordinates(x0, y0, distance, angle_degrees):
    angle_radians = math.radians(angle_degrees)  # Convert angle to radians

    # Calculate new coordinates
    x = x0 + distance * math.cos(angle_radians)
    y = y0 + distance * math.sin(angle_radians)

    # Explicit rounding to avoid floating-point precision issues
    return round(x), round(y)
