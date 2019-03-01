# Import libraries
import RPi.GPIO as GPIO
from gpiozero import PWMLED
from time import sleep
from signal import pause

# Write all codes inside try statement
try:
    led = PWMLED(17)
    led.blink(2,2)
    pause()

# except statement to handle user's keyboard interrupt
except KeyboardInterrupt:
    print("Stopping python script...")
    print("Cleaning up GPIO...")

# finally statement will run before exiting try statement
finally:
    GPIO.cleanup()
    print("Cleaning completed!")
    print("Exit program")

