from gpiozero import PWMLED, Button
from time import sleep

led = PWMLED(26)
button = Button(12)

button.wait_for_press()
led.value = 0.3
