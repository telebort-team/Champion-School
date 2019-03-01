from gpiozero import PWMLED
from time import sleep

led = PWMLED(17)
led2 = PWMLED(27)
led3 = PWMLED(22)

led.pulse(3,1)
sleep(1)
led2.pulse(3,1)
sleep(1)
led3.pulse(3,1)