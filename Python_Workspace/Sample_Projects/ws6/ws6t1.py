from picamera import PiCamera
from PIL import Image
import matplotlib.pyplot as plt
from time import sleep

camera = PiCamera()
sleep(2)
camera.capture("image.jpg")
camera.close()

im = Image.open("image.jpg")
plt.figure()
plt.imshow(im)
plt.show()

