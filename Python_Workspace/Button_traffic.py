# Import libraries
import RPi.GPIO as GPIO
from time import sleep
from gpiozero import LED, Button

# Write all codes inside try statement
try:
    button = Button(4)
    red = LED(17)
    yellow = LED(27)
    green = LED(22)
    
    while True:
        button.wait_for_press()
        red.on()
        sleep(1)
        red.off()
        yellow.on()
        sleep(1)
        yellow.off()
        green.on()
        sleep(1)
        green.off()

# except statement to handle user's keyboard interrupt
except KeyboardInterrupt:
    print("Stopping python script...")
    print("Cleaning up GPIO...")

# finally statement will run before exiting try statement
finally:
    GPIO.cleanup()
    print("Cleaning completed!")
    print("Exit program")