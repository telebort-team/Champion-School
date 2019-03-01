from gpiozero import LED, DistanceSensor
from time import sleep

led = LED(26)
sensor = DistanceSensor(echo=24, trigger= 23)

sensor.wait_for_in_range()
led.on()

