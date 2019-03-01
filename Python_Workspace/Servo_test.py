from gpiozero import Servo
from time import sleep

servo = Servo(26)
while True:
    servo.value = -1
    sleep(3)
    servo.value = 0
    sleep(3)
    servo.value = 1
    sleep(3)