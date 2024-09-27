import pyautogui
import keyboard
import time
time.sleep(3)
while keyboard.is_pressed("q") == False:
    pyautogui.click()