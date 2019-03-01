# Import libraries
import RPi.GPIO as GPIO
from time import sleep
from signal import pause
from gpiozero import RGBLED, MotionSensor

# Write all codes inside try statement
try:
    pir = MotionSensor(27)
    
    while True:
        pir.wait_for_motion()
        print("detected")
        sleep(0.5)

# except statement to handle user's keyboard interrupt
except KeyboardInterrupt:
    print("Stopping python script...")
    print("Cleaning up GPIO...")

# finally statement will run before exiting try statement
finally:
    pir.close()
    GPIO.cleanup()
    print("Cleaning completed!")
    print("Exit program")