from gpiozero import LED, Button
from time import sleep

led = LED(26)
button = Button(12)

button.wait_for_press()
sleep(3)
led.on()
