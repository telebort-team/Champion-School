from gpiozero import LED, Button
from time import sleep

led = LED(26)
button = Button(12)

button.wait_for_press()
led.on()
button.wait_for_release()
led.off()
