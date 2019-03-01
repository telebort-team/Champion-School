from gpiozero import LED, DistanceSensor
from time import sleep

led = LED(26)
sensor = DistanceSensor(echo=24, trigger= 23)

while True:
    if sensor.distance <= 0.3:
        led.on()
    else:
        led.off()

