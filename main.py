import pyautogui
import time
import os
from PIL import ImageGrab

# User settings
number = ""
text = ""

# Intermediate user settings
whatsapp_web_url = "https://web.whatsapp.com/"

# Advanced user settings
web_browser_path = "/usr/bin/google-chrome-stable"
terminal_command = "gnome-terminal '/bin/bash'"

# Only change if you know what you are doing
tabs = 5


def main():
    os.system(f"{terminal_command}")
    time.sleep(0.1)

    pyautogui.write(f"{web_browser_path}")
    pyautogui.press("enter")
    time.sleep(1)

    pyautogui.write(f"{whatsapp_web_url}")
    pyautogui.press("enter")

    while True:
        img = ImageGrab.grab()
        pixel = img.getpixel((130, 210))

        if pixel == (0, 134, 106):
            break
        else:
            time.sleep(1)

    time.sleep(2)

    for _ in range(tabs):
        pyautogui.press("tab")

    pyautogui.write(f"{number}")
    time.sleep(1)

    pyautogui.press("tab")
    pyautogui.press("tab")
    time.sleep(1)

    pyautogui.press("enter")
    time.sleep(1)

    pyautogui.write(f"{text}")
    pyautogui.press("enter")


if __name__ == '__main__':
    main()
