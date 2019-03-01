# Import libraries
import RPi.GPIO as GPIO
from time import sleep
from signal import pause
from gpiozero import RGBLED

# Write all codes inside try statement
try:
    led = RGBLED(17, 27, 22, active_high=False) # Set active_high to False for common anode
    led.pulse(on_color=(0.1,0.3,0.4))
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