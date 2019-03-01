from gpiozero import PWMLED, DistanceSensor
from time import sleep

led = PWMLED(26)
sensor = DistanceSensor(echo=24, trigger= 23)

while True:
    print("sensor = ", sensor.distance)
    led.value = 1 - sensor.distance
    print("led = ", led.value)
    sleep(0.5)

