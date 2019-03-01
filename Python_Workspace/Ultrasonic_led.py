from gpiozero import LED, DistanceSensor
from time import sleep

sleep(2)
led = LED(26)
sensor = DistanceSensor(trigger=23,echo=24)

while True:
    dist = sensor.distance * 100
    print(dist)
    if dist > 5:
        led.on()
    else:
        led.off()