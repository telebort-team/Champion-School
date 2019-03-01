from gpiozero import LED, Button
from time import sleep

led = LED(26)
button = Button(12)

button.wait_for_press()
button.wait_for_release()
led.blink(n=3)
