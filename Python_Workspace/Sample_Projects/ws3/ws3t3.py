from gpiozero import PWMLED, Button
from time import sleep

led = PWMLED(26)
button = Button(12)

while True:
    button.wait_for_press()
    led.pulse(n=1)
