import threading

# wheelWriteThrowback.py
leftPWMValue = 0
rightPWMValue = 0

def writePWM(number, leftOrRight):
    global leftPWMValue, rightPWMValue
    if leftOrRight == "left":
        leftPWMValue = number
    elif leftOrRight == "right":
        rightPWMValue = number

    


# Start the loop in a daemon thread so it doesn't block or hang the parent script
wwt_thread = threading.Thread(target=writePWM, args=(0, "left"), daemon=True)
wwt_thread.start()
    