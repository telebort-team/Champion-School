from gpiozero import PWMLED, Button
from time import sleep

led = PWMLED(26)
upButton = Button(12)
downButton = Button(25)

while True:
    sleep(0.5) # To reduce button bounce
    if upButton.is_pressed:
        led.value = led.value + 0.1
    elif downButton.is_pressed:
        led.value = led.value - 0.1
