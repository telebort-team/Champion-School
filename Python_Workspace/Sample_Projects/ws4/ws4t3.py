from gpiozero import LED, Button, LightSensor
from time import sleep

led = LED(23)
button = Button(26)
sensor = LightSensor(4, threshold=0.9) # Change threshold to lower sensitivity

while True:
    # print(sensor.light_detected)
    if not sensor.light_detected and button.is_pressed:
        led.on()
    else:
        led.off()
        
