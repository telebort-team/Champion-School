# Button expect active-Low config
# Avoid special function pins
import RPi.GPIO as GPIO
from gpiozero import LED, Button

# Write all codes inside try statement
try:
    led = LED(26)
    button = Button(13)
    while True:
        if button.is_pressed:
            led.on()
        else:
            led.off()

# except statement to handle user's keyboard interrupt
except KeyboardInterrupt:
    print("Cleaning up GPIO...")
    print("Stopping python script...")

# finally will run before exiting try statement
finally:
    GPIO.cleanup()