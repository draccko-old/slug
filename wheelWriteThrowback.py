leftPWMValue = 0
rightPWMValue = 0


def writePWM(number, leftOrRight):
    if leftOrRight == "left":
        leftPWMValue = number
    elif leftOrRight == "right":
        rightPWMValue = number
    else:
        raise ValueError("Invalid argument for leftOrRight. Use 'left' or 'right'.")
    