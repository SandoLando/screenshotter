from PIL import ImageGrab
import os
import time


# Takes screenshot of entire screen and saves it to desktop
time.sleep(3)
def screenGrab():
    box = ()
    im = ImageGrab.grab(box)
    im.save(os.getcwd() + "\\full_snap__" + str(int(time.time())) +
            ".png", "PNG")

if __name__ == ("__main__"):
    screenGrab()
