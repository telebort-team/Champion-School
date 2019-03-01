from gpiozero import LED
from time import sleep

led = LED(26)

sleep(3)
led.on()
