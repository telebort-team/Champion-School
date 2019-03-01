from picamera import PiCamera
from gpiozero import Button
from time import sleep

button = Button(26)
camera = PiCamera()

button.wait_for_press()
for i, filename in enumerate(camera.capture_continuous('image{counter}.jpg')):
    print(filename)
    sleep(0.5)
    if i == 4:
        break
camera.close()


