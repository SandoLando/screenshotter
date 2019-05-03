from PIL import ImageGrab
import os
import time


# Takes screenshot of entire screen and saves it to desktop
# For whatever reason, only works from IDLE
def screenGrab():
    while True:
        print("Press ENTER to take screenshots. Press Q to quit.")
        take_screenshot = input()
        if take_screenshot.upper() == 'Q':
            break
        else:
            box = ()
            im = ImageGrab.grab(box)
            im.save(os.getcwd() + "\\full_snap__" + str(int(time.time())) +
            ".png", "PNG")
            continue
        
        
if __name__ == "__main__":
    screenGrab()
    
