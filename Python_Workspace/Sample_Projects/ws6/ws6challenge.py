from picamera import PiCamera
from gpiozero import LightSensor, DistanceSensor
from time import sleep

light = LightSensor(13)
dist = DistanceSensor(echo=24,trigger=23)
camera = PiCamera()

while True:
    light.wait_for_dark()
    isDark = True
    while isDark:
        for frame in camera.capture_continuous('img-{timestamp:%H-%M-%S}.jpg'):
            print(frame)
            print('Distance = ', dist.distance)
            while dist.distance >= 0.3:
                sleep(1)
                isDark = not light.light_detected
                print('is dark = ', isDark)
                if not isDark:
                    break
            if not isDark:
                break
