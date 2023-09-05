#import pytesseract
import datetime
import pyautogui
from pynput import mouse
import time
import argparse
import numpy as np
#from PIL import Image
import pyperclip


import easyocr

class ClickListener:
    def __init__(self):
        self.click_count = 0
        self.coordinates = []

    def on_click(self, x, y, button, pressed):
        if pressed:
            self.click_count += 1
            self.coordinates.append((x, y))
            
            # Stop the listener after two clicks
            if self.click_count == 2:
                return False
    def getCoordinates(self):
        return self.coordinates


# Create an EasyOCR Reader instance
reader = easyocr.Reader(['ja'])

def capture_and_read(x, y, width, height, mask_type=None):
    # Capture the selected portion of the screen
    screenshot = pyautogui.screenshot(region=(x, y, width, height))
    
    # Convert the screenshot into an RGB format compatible with EasyOCR
    screenshot_rgb = screenshot.convert("RGB")
    screenshot_np = np.array(screenshot_rgb)

    # Apply mask based on the given argument
    if mask_type == 'black':
        mask = np.all(screenshot_np != [255, 255, 255], axis=-1)
        screenshot_np[mask] = [0, 0, 0]
    elif mask_type == 'white':
        mask = np.all(screenshot_np != [0, 0, 0], axis=-1)
        screenshot_np[mask] = [255, 255, 255]
    
    # Use EasyOCR to extract text
    results = reader.readtext(screenshot_np)
    
    # Combine the extracted text components
    text = ' '.join([result[1] for result in results])
    
    return text


def main():
    parser = argparse.ArgumentParser(description="Capture screen and apply mask based on given argument.")
    parser.add_argument('-s', '--mask', choices=['black', 'white'], help='Type of subtitles in video. Choose black for black subtitles')
    args = parser.parse_args()
    print("Please drag the mouse over the area you want to capture...")
    listener_instance = ClickListener()
    with mouse.Listener(on_click=listener_instance.on_click) as listener:
        listener.join()

    # Wait for mouse button down and then get the starting coordinates
    [(x1,y1),(x2,y2)] = listener_instance.getCoordinates()
    print("Capture area set")

    width, height = x2 - x1, y2 - y1
    
    while(True):
        extracted_text = capture_and_read(x1, y1, width, height)
        #print(extracted_text)
        pyperclip.copy(extracted_text)
        time.sleep(2)

if __name__ == '__main__':
    main()
