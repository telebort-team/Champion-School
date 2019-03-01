from gpiozero import Buzzer, DistanceSensor
from time import sleep

buzzer = Buzzer(12)
sensor = DistanceSensor(echo=24, trigger= 23)

while True:
    dist = sensor.distance * 100
    # print(dist)
    if dist >= 20:
        continue
    elif dist >= 15:
        buzzer.beep(on_time=0.3,off_time=0.3,n=1,background=False)
    elif dist >= 10:
        buzzer.beep(on_time=0.3,off_time=0.3,n=2,background=False)
    elif dist < 10:
        buzzer.on()
    else:
        buzzer.off()
    sleep(0.5)

