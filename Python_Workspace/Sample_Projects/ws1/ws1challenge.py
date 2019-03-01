from gpiozero import LED
from time import sleep

red = LED(26)
yellow = LED(23)
green = LED(24)

red.on()
sleep(2)
red.off()
yellow.on()
sleep(1)
yellow.off()
green.on()
sleep(3)
green.off()
