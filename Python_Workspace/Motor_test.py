from gpiozero import Motor
from time import sleep

motor = Motor(17, 27)
motor.forward(1)
sleep(5)
motor.stop()
sleep(1)
motor.backward(1)
sleep(3)
motor.stop()