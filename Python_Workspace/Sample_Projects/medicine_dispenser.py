from gpiozero import MotionSensor
from picamera import PiCamera
from time import sleep
from PIL import Image
import matplotlib.pyplot as plt
import time

pir = MotionSensor(4)

camera = PiCamera()
camera.vflip = True
camera.hflip = True

print('Program started!')

img = 0
COLUMNS = 3
ROWS = 2

while True:
    if pir.motion_detected:
        print('Motion Detected')
        fig = plt.figure()
        plt.title('Image taken time: ' + time.strftime('%Y-%m-%d %H:%M:%S'))
        plt.axis('off')

        index = 0
        while index < 6:
            camera.capture('/home/pi/Desktop/img/%s.jpg' % img)
            imgs = Image.open('/home/pi/Desktop/img/%s.jpg' % img).resize((256, 256))
            fig.add_subplot(ROWS, COLUMNS, index), plt.imshow(imgs)
            plt.axis('off')
            sleep(1)
            index += 1
            img += 1

        plt.show()
        print('6 photos capture in a time')

    else:
        print('Motion Not Detected')