from gpiozero import PWMLED
from time import sleep

led = PWMLED(26)

led.pulse(fade_in_time=2,fade_out_time=1,n=5)
