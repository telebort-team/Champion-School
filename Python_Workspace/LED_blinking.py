# Basic LED blinking
import RPi.GPIO as GPIO
from gpiozero import LED
from time import sleep

# Write all codes inside try statement
try:
    led = LED(17)
    
    while True:
        led.on()
        sleep(1)
        led.off()
        sleep(1)

# except statement to handle user's keyboard interrupt
except KeyboardInterrupt:
    print("Stopping python script...")
    print("Cleaning up GPIO...")

# finally will run before exiting try statement
finally:
    GPIO.cleanup()
    print("Cleaning completed!")
    print("Exit program")