# Import libraries
import RPi.GPIO as GPIO
from time import sleep
from signal import pause
from gpiozero import LED

# Write all codes inside try statement
try:


# except statement to handle user's keyboard interrupt
except KeyboardInterrupt:
    print("Stopping python script...")
    print("Cleaning up GPIO...")

# finally statement will run before exiting try statement
finally:
    GPIO.cleanup()
    print("Cleaning completed!")
    print("Exit program")