import pyautogui
import threading
import time
import keyboard

class AutoClicker:
    def __init__(self, click_interval=0.001):  # customize the 0.0001 (in seconds) based on how fast you want it to click
        self.running = False
        self.click_interval = click_interval  # Interval for clicks in seconds

    def start_clicking(self):
        while self.running:
            pyautogui.click()
            time.sleep(self.click_interval)  # Sleep for a very short duration

    def toggle(self):
        self.running = not self.running
        if self.running:
            print("Auto Clicker Started")
            self.click_thread = threading.Thread(target=self.start_clicking)
            self.click_thread.daemon = True  # Allow thread to exit when main program does
            self.click_thread.start()
        else:
            print("Auto Clicker Stopped")
            self.click_thread.join()

def main():
    auto_clicker = AutoClicker(click_interval=0.0001)  # customize the 0.0001 (in seconds) based on how fast you want it to click
    print("Press 'F8' to toggle the auto clicker on/off.")
    keyboard.add_hotkey('F8', auto_clicker.toggle)

    # Keep the program running
    keyboard.wait('esc')  # Press 'esc' to exit the program

if __name__ == "__main__":
    main()
