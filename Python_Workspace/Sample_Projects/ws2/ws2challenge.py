from gpiozero import LED, Button
from time import sleep
import random

button = Button(12)
led1 = LED(13)
led2 = LED(6)
led3 = LED(5)
led4 = LED(22)
led5 = LED(27)
led6 = LED(17)

button.wait_for_press()
random_number = random.randint(1,6)

if random_number == 1:
    led1.on()
elif random_number == 2:
    led1.on()
    led2.on()
elif random_number == 3:
    led1.on()
    led2.on()
    led3.on()
elif random_number == 4:
    led1.on()
    led2.on()
    led3.on()
    led4.on()
elif random_number == 5:
    led1.on()
    led2.on()
    led3.on()
    led4.on()
    led5.on()
else:
    led1.on()
    led2.on()
    led3.on()
    led4.on()
    led5.on()
    led6.on()
