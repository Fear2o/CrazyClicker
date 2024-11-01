# CrazyClicker

A simple Python-based auto-clicker tool that allows users to click at a speed of 10 clicks per second **(the max speed is 1000 CPS and the clicking speed depends on your hardware)**. Toggle the clicker on and off with a hotkey, and exit the program with another. Useful for automation tasks, testing, or for increasing speed in specific applications.

## Features

- **Auto Clicker:** Achieve up to 10 clicks per second with a minimal interval between each click. ( can go faster depending on your hardware )
- **Toggle Hotkey:** Start and stop clicking with the `F8` key. (can be customized)
- **Exit Hotkey:** Exit the program by pressing the `Esc` key. (can be customized)
- **Simple and Fast:** just clone the program and run the script without any extra steps and super easy to use.

## Requirements

- Python 3.x
- [pyautogui](https://pypi.org/project/PyAutoGUI/) – for controlling the mouse
- [keyboard](https://pypi.org/project/keyboard/) – for hotkey detection

Install dependencies with:

```bash
pip install pyautogui keyboard
```

## Usage

1. **Clone this repository and change to its directory**:

   ```bash
   git clone https://github.com/Fear2o/CrazyClicker
   cd CrazyClicker
   ```

2. **Make sure the dependencies are installed:**

```bash
pip install -r requirements.txt
```   

2. **Run The Script:**

```bash
python CrazyClicker.py
```


3. **Control the auto-clicker**:
   - Press `F8` to start or stop clicking.
   - Press `Esc` to exit the program.


## Code Overview

- **AutoClicker class**: Manages the clicking functionality.
  - `start_clicking`: Continuously clicks at the specified interval.
  - `toggle`: Starts or stops the clicking thread.
- **Main function**: Initializes the `AutoClicker` and sets up hotkeys.

## Notes

- Adjust the `click_interval` in the `AutoClicker` class if you need a different click speed.
- The `F8` key is used as the toggle hotkey, but this can be customized if needed.
- to customize the `F8` and `esc` keys you can modify the `keyboard.add_hotkey` and `keyboard.wait` classes, both can be found in the code at line 30 and 33



