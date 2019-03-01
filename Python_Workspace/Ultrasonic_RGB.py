# Import libraries
import RPi.GPIO as GPIO
from time import sleep
from signal import pause
from gpiozero import LED, DistanceSensor

# Write all codes inside try statement
try:
    led = LED(17)
    sensor = DistanceSensor(trigger=4,echo=26)
    
    while True:
        dist = sensor.distance * 100
##        print('Distance to nearest object is', dist, 'cm')
        
        if dist < 50:
            led.on()
        else:
            led.off()
#        sleep(0.1)


# except statement to handle user's keyboard interrupt
except KeyboardInterrupt:
    print("Stopping python script...")
    print("Cleaning up GPIO...")

# finally statement will run before exiting try statement
finally:
    sensor.close()
    GPIO.cleanup()
    print("Cleaning completed!")
    print("Exit program")