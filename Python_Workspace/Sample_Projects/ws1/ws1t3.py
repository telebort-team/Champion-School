from gpiozero import LED
from time import sleep
from signal import pause

led = LED(26)
led2 = LED(23)

led2.blink(on_time=2, off_time=1)

led.on()
sleep(3)
led.off()

pause()
