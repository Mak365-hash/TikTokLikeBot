from pynput.mouse import Button, Controller
import time
mouse = Controller()

time.sleep(5)

while True:
    mouse.press(Button.left)
    mouse.release(Button.left)
    time.sleep(65)
    mouse.press(Button.left)
    mouse.release(Button.left)
    time.sleep(65)
