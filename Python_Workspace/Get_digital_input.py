from gpiozero import DigitalInputDevice
from time import sleep

device = DigitalInputDevice(26)

while True:
    print(device.value)
    sleep(1)