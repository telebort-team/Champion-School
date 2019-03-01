import RPi.GPIO as GPIO
from gpiozero import LED, DistanceSensor
from time import sleep

# Write all codes inside try statement
try:
    sensor = DistanceSensor(trigger=4,echo=26)

    while True:
        print('Distance to nearest object is', sensor.distance, 'm')
        sleep(1)

# except statement to handle user's keyboard interrupt
except KeyboardInterrupt:
    print("Cleaning up GPIO...")
    print("Stopping python script...")

# finally will run before exiting try statement
finally:
#    GPIO.cleanup()
    sensor.close()
    led.close()
    
