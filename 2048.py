import keyboard
import time

order = [
    "up",
    "left",
    "down",
    "right"
]

time.sleep(3)

while True:
    for i in order:
        
        #press arrow keys
        keyboard.press_and_release(i)
        
        
        if keyboard.is_pressed("q"):
            break
        time.sleep(0.1)