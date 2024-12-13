"""
tab_key.py
Simulates Tab key presses based on cursor inactivity.

Copyright (c) 2024 @md-naciri. All rights reserved.

Version: 1.0.0
Created: 2024-12-13
Author: @md-naciri

Licensed under the MIT License.
"""

from pynput.keyboard import Controller as KeyboardController, Key
from pynput.mouse import Controller as MouseController
import time

__version__ = "1.0.0"
__author__ = "md-naciri"
__copyright__ = "Copyright (c) 2024 md-naciri. All rights reserved."

def show_metadata():
    print("Tab Key Simulation Script")
    print(f"Version: {__version__}")
    print(f"Author: {__author__}")
    print(__copyright__)


def simulate_keyboard_activity():
    """Simulates a Tab key press every 10 seconds if the cursor is stationary."""
    keyboard = KeyboardController()
    mouse = MouseController()

    last_position = mouse.position

    while True:
        time.sleep(10)  # Wait for 10 seconds
        current_position = mouse.position

        if current_position == last_position:
            keyboard.press(Key.tab)  # Use Key.tab for the Tab key
            keyboard.release(Key.tab)  # Release the Tab key
            print("Cursor is stationary. Tab key pressed. Keeping activity alive.")
        else:
            print("Cursor is in motion. Checking again in 10 seconds.")

        last_position = current_position


if __name__ == "__main__":
    show_metadata()
    try:
        simulate_keyboard_activity()
    except KeyboardInterrupt:
        print("Program exited.")
