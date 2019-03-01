from gpiozero import LED, LightSensor
from time import sleep

led = LED(23)
sensor = LightSensor(4, threshold=0.9) # Change threshold to lower sensitivity

sensor.wait_for_dark()
led.on()

