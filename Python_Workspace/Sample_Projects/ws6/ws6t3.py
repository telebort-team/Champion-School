from picamera import PiCamera
from PIL import Image
import matplotlib.pyplot as plt
from gpiozero import Button, LightSensor
from time import sleep

button = Button(26)
sensor = LightSensor(13)
camera = PiCamera()

while True:
    print(sensor.light_detected)
    if button.is_pressed and sensor.light_detected:
        camera.capture('image.jpg')
        break

im = Image.open("image.jpg")
plt.figure()
plt.imshow(im)
plt.show()

camera.close()



