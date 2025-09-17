import pyautogui
import time

# Open the command prompt
pyautogui.hotkey("win", "r")
pyautogui.write("cmd")
pyautogui.press("enter")

# List of color codes for the command prompt
colors = ["12", "13", "14", "15", "16", "17", "18", "19", "1A", "1B", "1C", "1D", "1E"]

# Infinite loop to repeat the colors
while True:
    for color in colors:
        pyautogui.write(f"color {color}")
        pyautogui.press("enter")  # Pause for half a second between each color change
